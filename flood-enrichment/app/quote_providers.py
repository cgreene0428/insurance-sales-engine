"""
Flood-quote portal automation (Playwright).

Both Private Market Flood and Argenia are QUOTE PORTALS, not APIs: you drive a
web form (Argenia behind a login) to produce a flood quote number, which then
goes onto the HubSpot deal record as a note (see hubspot_client.add_note_to_deal).

STATUS: SKELETON. The site-specific details — URLs, field/dropdown selectors,
the values to pick, and where the quote number renders — are unknown until a
real session (HAR / recording / written walkthrough) is captured. Every such
detail below is a placeholder marked TODO and guarded by _require(), so an
unconfigured provider raises a clear error instead of silently returning garbage.

Nothing here runs from the current sandbox: the network policy blocks
argenia.com / privatemarketflood.com. Run where those hosts are reachable.

Fill-in checklist per provider:
  1. Set the URL constant(s).
  2. Set each entry in SELECTORS to a real CSS/text selector.
  3. Implement the marked steps in _run_flow(): which dropdowns get which values
     (from `property_data`), the submit action, and how to read the quote number.
"""

from typing import Optional

from . import config
from . import hubspot_client

# Sentinel for "not yet filled in from a real session".
_TODO = ""

_HEADLESS = True
_NAV_TIMEOUT_MS = 30_000


class QuoteProviderError(RuntimeError):
    """Raised when a provider is misconfigured or a quote can't be produced."""


def _require(value, what: str):
    """Guard a placeholder: raise loudly if a site-specific detail is still TODO."""
    if value is None or value == _TODO:
        raise QuoteProviderError(
            f"{what} is not configured yet. Capture a real session (HAR / recording) "
            f"and fill in the selector/URL in quote_providers.py before running."
        )
    return value


class _BaseQuoteProvider:
    name = "base"
    # Subclasses fill these from a captured session.
    URL = _TODO
    SELECTORS: dict = {}

    def get_flood_quote(self, property_data: dict) -> str:
        """Open a browser, run the site flow, return the quote number string."""
        # Lazy import so the module compiles/loads without Playwright installed.
        try:
            from playwright.sync_api import sync_playwright
        except ImportError as exc:  # pragma: no cover
            raise QuoteProviderError(
                "playwright is not installed (pip install -r requirements.txt && "
                "playwright install chromium)"
            ) from exc

        _require(self.URL, f"{self.name}: quote page URL")
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=_HEADLESS)
            try:
                page = browser.new_page()
                page.set_default_timeout(_NAV_TIMEOUT_MS)
                page.goto(self.URL)
                quote = self._run_flow(page, property_data)
                if not quote:
                    raise QuoteProviderError(f"{self.name}: no quote number scraped")
                return quote.strip()
            finally:
                browser.close()

    def _run_flow(self, page, property_data: dict) -> Optional[str]:
        raise NotImplementedError


class PrivateMarketFloodProvider(_BaseQuoteProvider):
    """privatemarketflood.com — public quote form, no login."""

    name = "private_market_flood"
    URL = _TODO  # TODO: quote form URL
    SELECTORS = {
        # TODO: one entry per dropdown/field, e.g. "state": "#state-select"
        # "construction": "#construction",
        "submit": _TODO,        # TODO: submit button selector
        "quote_number": _TODO,  # TODO: element that shows the quote number
    }

    def _run_flow(self, page, property_data: dict) -> Optional[str]:
        # TODO from captured session: for each dropdown, select the value derived
        # from property_data, e.g.:
        #   page.select_option(_require(self.SELECTORS.get("state"), "PMF state"),
        #                      property_data.get("state"))
        page.click(_require(self.SELECTORS.get("submit"), "PMF submit button"))
        return page.inner_text(
            _require(self.SELECTORS.get("quote_number"), "PMF quote-number element")
        )


class ArgeniaProvider(_BaseQuoteProvider):
    """argenia.com — flood quote behind a username/password login."""

    name = "argenia"
    URL = _TODO        # TODO: login page URL
    QUOTE_URL = _TODO  # TODO: quote form URL after login (if different)
    SELECTORS = {
        "username": _TODO,      # TODO: username field selector
        "password": _TODO,      # TODO: password field selector
        "login_submit": _TODO,  # TODO: login button selector
        # TODO: quote form fields/dropdowns
        "submit": _TODO,        # TODO: quote submit button
        "quote_number": _TODO,  # TODO: element that shows the quote number
    }

    def _run_flow(self, page, property_data: dict) -> Optional[str]:
        if not config.ARGENIA_USERNAME or not config.ARGENIA_PASSWORD:
            raise QuoteProviderError("ARGENIA_USERNAME / ARGENIA_PASSWORD not set (.env)")
        # Login
        page.fill(_require(self.SELECTORS.get("username"), "Argenia username field"),
                  config.ARGENIA_USERNAME)
        page.fill(_require(self.SELECTORS.get("password"), "Argenia password field"),
                  config.ARGENIA_PASSWORD)
        page.click(_require(self.SELECTORS.get("login_submit"), "Argenia login button"))
        # Navigate to quote form if it's a separate page
        if self.QUOTE_URL and self.QUOTE_URL != _TODO:
            page.goto(self.QUOTE_URL)
        # TODO from captured session: fill the quote form fields/dropdowns from
        # property_data, then submit.
        page.click(_require(self.SELECTORS.get("submit"), "Argenia submit button"))
        return page.inner_text(
            _require(self.SELECTORS.get("quote_number"), "Argenia quote-number element")
        )


PROVIDERS = {
    PrivateMarketFloodProvider.name: PrivateMarketFloodProvider,
    ArgeniaProvider.name: ArgeniaProvider,
}


def quote_to_deal_note(deal_id: str, property_data: dict, provider_name: str) -> str:
    """Get a flood quote from `provider_name` and attach it to the HubSpot deal.

    Returns the quote number. Raises QuoteProviderError / HubSpotError on failure.
    """
    provider_cls = PROVIDERS.get(provider_name)
    if provider_cls is None:
        raise QuoteProviderError(
            f"unknown provider '{provider_name}'; known: {sorted(PROVIDERS)}"
        )
    quote = provider_cls().get_flood_quote(property_data)
    hubspot_client.add_note_to_deal(
        deal_id, f"Flood quote ({provider_name}): {quote}"
    )
    return quote
