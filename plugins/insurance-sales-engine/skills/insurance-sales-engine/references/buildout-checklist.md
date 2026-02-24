# AgencyZoom Buildout Checklist

Complete implementation checklist organized by phase. Work through each phase in order. Each item should be verified before moving to the next.

---

## Phase 1: Foundation (Week 1)

### Agency Discovery
- [ ] Complete agency profile questionnaire (team size, lines, AMS, lead sources)
- [ ] Document current sales process and pain points
- [ ] Identify current retention rate and biggest retention challenges
- [ ] Catalog existing marketing content and email templates
- [ ] Define success metrics and 90-day goals
- [ ] Identify brand voice (formal vs. conversational, tone, personality)

### BrandScript
- [ ] Complete Trust and Grow BrandScript for primary audience (personal lines)
- [ ] Complete BrandScript for commercial lines (if applicable)
- [ ] Agency owner has reviewed and approved BrandScripts
- [ ] Extract key messaging elements: tagline, one-liner, 3-step plan, CTAs

### AMS Integration
- [ ] Connect AgencyZoom to AMS (AMS360, Hawksoft, NowCerts, QQCatalyst, etc.)
- [ ] Verify two-way data sync is working
- [ ] Map fields between AMS and AgencyZoom
- [ ] Test sync with a sample record

---

## Phase 2: Pipeline Setup (Week 2)

### Sales Pipelines
- [ ] Create Personal Lines sales pipeline with stages: New Lead â Contacted â Needs Analysis â Quoted â Follow-Up â Sold â Lost
- [ ] Create Commercial Lines sales pipeline with stages: New Lead â Contacted â Discovery â Submission â Quoted â Negotiation â Bound â Lost
- [ ] Create Dream 100 pipeline with stages: Identified â First Touch â Engaged â Meeting Set â Relationship Active â Converted
- [ ] Customize stage names to match agency's language (if preferred)

### Service Pipelines
- [ ] Configure Onboarding pipeline: Welcome â Documents Collected â Policy Review Scheduled â Review Complete â Fully Onboarded
- [ ] Configure Renewal pipeline: 90-Day Review â Remarketed â Renewal Quoted â Renewal Presented â Renewed â Lost to Competitor
- [ ] Configure Service pipeline: New Request â In Progress â Waiting on Carrier â Waiting on Client â Resolved
- [ ] Configure Claims pipeline: Claim Reported â Adjuster Assigned â In Progress â Settlement â Closed

### Lead Source Configuration
- [ ] Add all lead sources (website, referral, purchased leads, walk-ins, events, etc.)
- [ ] Map each lead source to the correct pipeline
- [ ] Configure lead assignment rules (round-robin, territory, line of business)

---

## Phase 3: Content Creation (Weeks 2-4)

### Big 5 Content â Pricing
- [ ] Article: "How Much Does Homeowners Insurance Cost in [Area]?"
- [ ] Article: "Auto Insurance Costs Explained: What Actually Drives Your Premium"
- [ ] Article: "Commercial Insurance Pricing: What Business Owners Need to Know"
- [ ] Article: "Understanding Deductibles: How to Choose the Right One"
- [ ] Article: "Why the Cheapest Insurance Quote Isn't Always the Best Deal"

### Big 5 Content â Problems & Negatives
- [ ] Article: "5 Things Your Insurance Agent Probably Isn't Telling You"
- [ ] Article: "The Most Common Claim Mistakes and How to Avoid Them"
- [ ] Article: "When Bundling Insurance Actually Costs You More"
- [ ] Article: "Why Claims Get Denied: Top Reasons and Prevention"

### Big 5 Content â Comparisons
- [ ] Article: "Independent Agent vs. Captive Agent: Which Is Right for You?"
- [ ] Article: "Replacement Cost vs. Actual Cash Value Explained"
- [ ] Article: "HO3 vs. HO5: Which Homeowners Policy Do You Need?"

### Big 5 Content â Reviews
- [ ] Article: Review of top 2-3 carriers you represent
- [ ] Article: Client testimonials / success stories page

### Big 5 Content â Best in Class
- [ ] Article: "Best Homeowners Insurance in [Area]"
- [ ] Article: "Best Commercial Insurance for [Industry]"

### Lead Magnets (Transitional CTAs)
- [ ] Create: P&C Coverage Checklist
- [ ] Create: "5 Questions to Ask Before You Renew" guide
- [ ] Create: Home Inventory Worksheet

---

## Phase 4: Automation Build (Weeks 3-5)

### Prospecting Automation
- [ ] Build New Lead stage automation (text + email + task sequence)
- [ ] Build Contacted stage automation (needs analysis follow-up)
- [ ] Build Quoted stage automation (quote follow-up + content sequence)
- [ ] Build Follow-Up stage automation (nurture sequence before Smart Cycle)
- [ ] Build Lost stage automation (graceful exit + Smart Cycle enrollment)
- [ ] Configure Smart Cycle for unsold lead recycling
- [ ] Set auto-unenroll on reply = ON for prospecting

### Onboarding Automation
- [ ] Build Welcome stage automation (welcome email + text + call task)
- [ ] Build Documents Collected stage automation (checklist + reminders)
- [ ] Build Policy Review stage automation (scheduling + prep content)
- [ ] Build Review Complete stage automation (summary + cross-sell intro)
- [ ] Build Fully Onboarded stage automation (celebration + review request)
- [ ] Set auto-unenroll on reply = OFF for onboarding

### Renewal Automation
- [ ] Build 90-Day Review automation (notification + client email + content)
- [ ] Build Remarketed automation (status updates)
- [ ] Build Renewal Quoted automation (schedule review)
- [ ] Build Renewal Presented automation (follow-up sequence)
- [ ] Build Renewed automation (confirmation + cross-sell + referral request)
- [ ] Build Lost to Competitor automation (exit + win-back enrollment)

### Service & Claims Automation
- [ ] Build Service request acknowledgment automation
- [ ] Build Claims first-response automation
- [ ] Build Claims status update automation (weekly)
- [ ] Build Claims closed follow-up automation

### Dream 100 Automation
- [ ] Build First Touch automation (personalized intro sequence)
- [ ] Build Engaged nurture automation (bi-weekly value delivery)
- [ ] Set reminders for manual touchpoints (lunch, events, calls)

---

## Phase 5: Templates & Content Library (Week 4-5)

### Email Templates
- [ ] Load all prospecting email templates into Content Library
- [ ] Load all onboarding email templates
- [ ] Load all renewal email templates
- [ ] Load all service/claims email templates
- [ ] Load all Dream 100 email templates
- [ ] Load referral request email template
- [ ] Load review request email template
- [ ] Load cross-sell introduction templates

### Text Templates
- [ ] Load all text message templates
- [ ] Verify text templates are under 160 characters where possible
- [ ] Test personalization tokens ({First Name}, {Agent Name}, etc.)

### Task Templates
- [ ] Define standard task descriptions for recurring tasks
- [ ] Set default assignees for each task type

---

## Phase 6: Dashboard & Reporting (Week 5)

### Producer Dashboard
- [ ] Configure Today's Tasks widget
- [ ] Configure Pipeline Overview widget
- [ ] Configure Hot Leads / engagement widget
- [ ] Configure Close Rate tracker
- [ ] Set up new lead notification alerts

### CSR / Account Manager Dashboard
- [ ] Configure Service Requests widget
- [ ] Configure Onboarding Pipeline widget
- [ ] Configure Renewal Calendar widget (30/60/90 day view)
- [ ] Configure Cross-Sell Opportunities widget
- [ ] Set up renewal and claims alerts

### Agency Owner Dashboard
- [ ] Configure Revenue Summary widget
- [ ] Configure Producer Leaderboard widget
- [ ] Configure Retention Rate tracker
- [ ] Configure Lead Source ROI widget
- [ ] Configure Automation Performance metrics
- [ ] Set up monthly report auto-generation

---

## Phase 7: Testing & QA (Week 6)

### Test Flows
- [ ] Run test lead through FULL prospecting â quoting â onboarding flow
- [ ] Verify every email/text fires at correct timing
- [ ] Verify all personalization tokens populate correctly
- [ ] Verify tasks assign to correct team members
- [ ] Verify Smart Cycle enrollment works for lost leads
- [ ] Run test client through renewal flow
- [ ] Run test client through claims flow
- [ ] Verify dashboards update in real-time

### Copy Review
- [ ] Read every email sequence from the PROSPECT'S perspective
- [ ] Check: Does it feel personal (A-pile) or like marketing (B-pile)?
- [ ] Check: Is each email's purpose clear? One CTA per email?
- [ ] Check: Does the emotional arc match the awareness stage?
- [ ] Check: Are there any "dead zones" where the prospect hears nothing for too long?
- [ ] Check: Are there any sequences that feel too aggressive or too frequent?

### Settings Verification
- [ ] Business Days Only toggle set correctly per workflow
- [ ] Auto-unenroll on reply configured correctly (ON for prospecting, OFF for onboarding)
- [ ] Lead source mapping verified
- [ ] AMS sync verified with live data
- [ ] Notification preferences set for all team members

---

## Phase 8: Launch & Training (Week 6-7)

### Team Training
- [ ] Producer training: Pipeline workflow, daily task routine, assignment selling
- [ ] CSR training: Service/claims pipeline, onboarding workflow, renewal workflow
- [ ] Owner training: Dashboard overview, reporting, performance monitoring
- [ ] All team members: How to use the Content Library and templates

### Go-Live Checklist
- [ ] All automation toggles set to ACTIVE (Blue = ON)
- [ ] All existing leads imported and placed in correct pipeline stages
- [ ] All existing clients imported with correct renewal dates
- [ ] Team calendar blocked for "AgencyZoom day 1" support
- [ ] 30-day check-in scheduled to review performance and adjust

### Post-Launch (30/60/90 Day Reviews)
- [ ] 30-day review: Email open rates, task completion rates, pipeline movement
- [ ] 30-day review: Gather team feedback on workflows
- [ ] 60-day review: Close rate comparison (before vs. after)
- [ ] 60-day review: Retention rate tracking
- [ ] 90-day review: Full ROI assessment
- [ ] 90-day review: Content gap analysis (which Big 5 topics need more content?)
- [ ] Ongoing: Monthly automation performance review and copy optimization
