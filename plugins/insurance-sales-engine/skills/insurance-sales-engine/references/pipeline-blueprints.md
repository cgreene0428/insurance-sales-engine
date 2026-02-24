# AgencyZoom Pipeline Blueprints for P&C Agencies

Every stage in every pipeline is defined through TWO lenses:

- **CX (Customer Experience)*: What does the customer see, feel, and receive?
- **EX (Employee Experience)*: What does the team member DO? Every task must be specific enough that no one wastes a single second figuring out what to do. If an employee has to think "what does this task mean?" â the buildout failed.

**EX Task Rules:**
- Every task description tells the employee EXACTLY what to do, WHO to contact, and WHAT to say or reference
- Time estimates on every task (2 min, 5 min, 15 min, 30 min)
- "Done" criteria on every task â o what does completing this look like?
- Escalation built in â if a task sits untouched for 24h, a reminder fires. 48h, it escalates.
- Talking points embedded in task descriptions so the employee never opens a task and goes "uh... what do I say?"

---

## Sales Pipeline â Personal Lines

### Stage: New Lead
**Duration**: 0-24 hours
**Goal**: Make first contact and establish yourself as the guide

#### CX (What the customer experiences):
- Within 5 minutes of submitting: a personal text from a real person (not a bot)
- Within 15 minutes: a helpful email with educational content â not a sales pitch
- Emotional tone: "We see you, we're here, zero pressure"
- The customer should think: "Wow, that was fast. And they didn't just try to sell me â they sent me something useful."

#### EX (What the employee does):

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Immediate | Auto-assign | Lead auto-assigned to producer based on rules. Producer gets push notification. | 0 min | Auto |
| 2 | 5 min | Auto text | System sends: "Hey {First Name}! This is {Agent Name} at {Agency Name}. I just saw your quote request â I'd love to help. Is now a good time for a quick 5-min call, or is there a better time today?" | 0 min | Auto |
| 3 | 15 min | Auto email | System sends welcome email with pricing article link | 0 min | Auto |
| 4 | 4 hours | Task: Call | **"Call {First Name} ({Phone}) â new {Lead Source} lead for {Policy Type}. They submitted at {Time}. Open their profile, check what content they clicked. Say: 'Hey {First Name}, this is {Agent Name} â I sent you a text earlier. Just wanted to put a voice to the name. Do you have 5 minutes to tell me what you're looking for?'"** | 5 min | Log call notes in AgencyZoom. If connected â move to Contacted. If voicemail â log "VM left" and leave in New Lead. |
| 5 | Next biz day | Auto email | Follow-up email if still in New Lead: "Hey {First Name}, just following up..." | 0 min | Auto |
| 6 | 48 stale | Reminder | **"STALE LEAD: {First Name} has been in New Lead for 48h with no contact. Try: text, call, email â in that order. If no response after 3 attempts across 2 channels, move to Follow-Up stage."** | 2 min | Contact made or moved to Follow-Up |

**Escalation**: If lead sits in New Lead for 72h â alert to team lead/manager.

**Copy approach**: Schwartz Level 2-3 awareness. Personal (Halbert A-pile). Name their likely situation.

(*Email template:**
```
Subject: {First Name}, quick intro + something useful

Hey {First Name},

I'm {Agent Name} at {Agency Name} â your quote request just landed on my desk and I wanted to reach out personally.

Before we jump into numbers, I put together a quick guide that covers what actually drives your premium and how to make sure you're not overpaying:

[Link: How Much Does Homeowners Insurance Cost in {Area}?]

I'll follow up with a call later today, but no pressure â I'm here whenever you're ready.

{Agent Name}
{Phone}
```

---

### Stage: Contacted
**Duration**: 1-3 days
**Goal**: Complete needs discovery, build rapport

#### CX:
- The customer just had a real conversation with their agent. They felt heard.
- Within 1 day, they receive educational content that reinforces why an independent agent is the right choice
- Emotional tone: "This person listened to me and now they're educating me â not selling me"

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | After contact | Task: Data entry | **"Complete needs analysis for {First Name}: Open their record. Fill in: current carrier, current premium, property details, vehicles, household members, pain points they mentioned on the call. Check: do we have dec pages? If not, request them NOW (use the dec page request template in Content Library)."** | 10 min | All fields populated, dec pages requested if missing |
| 2 | 1 biz day | Auto email | System sends: "Independent Agent vs. Captive Agent" comparison article | 0 min | Auto |
| 3 | 2 biz days | Reminder | **"Needs analysis incomplete for {First Name}. Missing: [list fields]. Call/text to collect remaining info. Say: 'Hey {First Name}, I'm putting your quote together and want to make sure I get you the best rate. Can you send me [missing item]?'"** | 5 min | Needs analysis complete â move to Needs Analysis |

---
Update status to Sold. 2) Enter policy details. 3) Assign to onboarding CSR/AM. 4) Send personal text: 'Welcome to {Agency Name}, {First Name}! I'm thrilled to have you. You're going to hear from {CSR Name} â she'll take amazing care of you from here.' 5) Move to Onboarding pipeline."** | 5 min | Client in Onboarding pipeline, CSR assigned |

---

### Stage: Lost
**Duration**: Ongoing via Smart Cycle

#### CX:
- Graceful, dignified farewell. No guilt trips. Door stays wide open.
- They think: "That was classy. I'd go back to them."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Immediate | Task: Log reason | **"Record loss reason for {First Name}. Select from: Price, Went with incumbent, Went with competitor, Bad timing, No response, Other. Add any notes from conversations. This data matters â we review lost reasons monthly to improve."** | 2 min | Reason logged |
| 2 | 1 biz day | Auto email | Gracious farewell email (see template below) | 0 min | Auto |
| 3 | Immediate | Auto | Enroll in Smart Cycle for long-term nurture and re-engagement | 0 min | Auto |

**Farewell email template:**
```
Subject: No hard feelings, {First Name}

Hey {First Name},

I understand you went a different direction â no worries at all. I hope you got great coverage.

If anything changes, or if you just want a second opinion down the road, I'm always here. Even if you just have a question about a claim or want someone to look over your policy â don't hesitate.

Wishing you and your family the best,
{Agent Name}
```

---

## Onboarding Pipeline

### Stage: Welcome (Days 1-3)
**Goal**: Eliminate buyer's remorse, set expectations, make them feel like VIPs

#### CX:
- Day 0: Welcome email that paints the picture of success (Trust and Grow narrative element 7)
- Day 1: Personal text from their account manager â "Hi, I'm {CSR Name}, I'll be your go-to"
- Day 2: "What to expect in your first 30 days" educational email
- Day 3: Welcome call from account manager
- They think: "Wow, I've never been treated this well by an insurance agency. I made a great choice."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Day 0 | Auto email | Welcome email: what happens next, who their contacts are, how to reach us | 0 min | Auto |
| 2 | Day 1 | Auto text | CSR introduction text: "Hi {First Name}! I'm {CSR Name} at {Agency Name} â I'll be your point person for anything you need. Save this number! ð" | 0 min | Auto |
| 3 | Day 2 | Auto email | "What to Expect in Your First 30 Days" article | 0 min | Auto |
| 4 | Day 3 | Task: Welcome call | **"Welcome call to {First Name} ({Phone}). Intro yourself as their account manager. Cover: 1) Confirm they received their policy docs and ID cards. 2) Ask if they have any questions about coverage. 3) Explain how to file a claim (don't wait for them to ask). 4) Set up their online account access if needed. 5) Ask: 'Is there anything else you need protected that we should talk about?' (natural cross-sell opening). Log notes."** | 10 min | Call completed, notes logged |

**Important**: Auto-unenroll on reply = OFF for onboarding. They should get everything.

---

### Stage: Documents Collected (Days 3-7)
**Goal**: Get everything needed to fully service the account

#### CX:
- Clear, simple instructions on what to send and how
- Patient follow-ups â never frustrated or demanding
- They think: "This is easy. They made it simple for me."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Day 3 | Auto email | Document checklist email: "Here's what we need to fully set up your account: [list]. You can email, text a photo, or drop by â whatever's easiest." | 0 min | Auto |
| 2 | Day 5 | Reminder | **"Documents outstanding for {First Name}. Missing: [list]. Text them: 'Hey {First Name}, just a quick reminder â we're still missing [X]. You can snap a photo and text it to me. Takes 30 seconds!' Keep it light and easy."** | 2 min | Text sent |
| 3 | Day 7 | Task: Call | **"Call {First Name} ({Phone}) â docs still missing. This is a service call, not a chase call. Say: 'Just calling to check in and make sure everything's going smooth. By the way, we still need [X] to finish setting up your account â can I walk you through how to find it?'"** | 5 min | All docs received â move to Policy Review Scheduled |

---

### Stage: Policy Review Scheduled (Days 7-14)
**Goal**: Schedule and conduct comprehensive policy review

#### CX:
- They receive a scheduling link â easy, no back-and-forth
- Pre-review content so they come prepared (assignment selling)
- They think: "My agent actually wants to sit down and make sure I'm covered. Nobody else did this."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Day 7 | Auto email | Scheduling link + "5 Questions to Ask During Your Policy Review" article | 0 min | Auto |
| 2 | Day 9 | Auto text | "Hey {First Name}, did you get a chance to schedule your policy review? Here's the link again: [Link]. It's a 15-min call â worth every second." | 0 min | Auto |
| 3 | Pre-review | Task: Prep | **"Prepare for policy review with {First Name}. Pull up: current coverages, any gaps identified during quoting, cross-sell opportunities (umbrella? life? auto if not already?). Create a one-page summary showing: what's covered, recommended improvements, estimated cost of improvements. Have this ready BEFORE the call."** | 15 min | Summary prepared |
| 4 | Review day | Task: Conduct review | **"Policy review call with {First Name}. Walk through: 1) Current coverages â confirm they understand what they have. 2) Any gaps or recommendations. 3) Cross-sell needs â frame as: 'Based on your situation, here's something to consider when the time is right.' 4) How to file a claim, who to call. 5) Set expectations for renewal process. Log notes. Move to Review Complete."** | 15 min | Review completed, notes logged, moved to Review Complete |

---

### Stage: Review Complete (Days 14-21)
**Goal**: Confirm all is set, plant cross-sell seeds naturally

#### CX:
- Summary email of everything discussed â they have it in writing
- Educational cross-sell content â not a pitch, just information for when they're ready
- They think: "This is the most organized, thorough insurance experience I've ever had."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Post-review | Task: Summary | **"Send policy review summary to {First Name}. Use template 'Post-Review Summary' from Content Library. Include: what was reviewed, any changes made or recommended, cross-sell items discussed (with no pressure), and your direct contact info."** | 5 min | Summary sent |
| 2 | Day 17 | Auto email | Cross-sell educational article (umbrella, life, etc.) â framed as "for when you're ready" | 0 min | Auto |
| 3 | Day 21 | Task: Verify | **"Verify all changes from review are processed for {First Name}. Check: endorsements processed? New policies bound? AMS updated? If all clear â move to Fully Onboarded."** | 5 min | Everything processed, moved to Fully Onboarded |

---

### Stage: Fully Onboarded (Day 21-30)
**Goal**: Celebrate, request review, transition to retention

#### CX:
- "You're all set!" celebration â they feel accomplished
- Google review request (with direct link â make it effortless)
- They think: "That was the best experience. I'm telling my friends."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Day 21 | Auto email | "You're all set" celebration email + introduce ongoing service team | 0 min | Auto |
| 2 | Day 25 | Auto email | Google review request with direct link. "If you had a good experience, a quick review helps other families find us: [Direct Link]" | 0 min | Auto |
| 3 | Day 30 | Auto text | "Hey {First Name}! How's everything going? Anything I can help with? â {CSR Name}" | 0 min | Auto |
| 4 | Day 30 | Task: Close out | **"Onboarding complete for {First Name}. Verify: 1) All docs collected. 2) Review completed. 3) Cross-sell opportunities noted for future. 4) Referral ask made or scheduled. Close onboarding. Client enters normal retention/renewal cycle."** | 2 min | Onboarding closed |

---

## Renewal Pipeline

### Stage: 90-Day Review
**Goal**: Get ahead of renewal, start shopping early, set expectations

#### CX:
- 90 days out: Proactive email â "We're already working on your renewal"
- Educational content about what's driving rates this year
- They think: "My agent is on top of this before I even had to think about it. They're shopping for me."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | 90 days out | Task: Begin remarket | **"Renewal trigger for {First Name} â {Policy Type} renews on {Date}. 1) Pull current policy details. 2) Check for any life changes (new home, new car, new family member). 3) Note if any claims in past year. 4) Begin remarketing process â submit to carriers this week."** | 10 min | Remarketing initiated |
| 2 | 90 days out | Auto email | "Your renewal is coming up â here's what we're doing" + market conditions article | 0 min | Auto |
| 3 | 80 days out | Auto email | Assignment selling: "What's Driving Insurance Rates in 2026" | 0 min | Auto |

**Escalation**: If no remarketing activity by 80 days out â manager alert.

---

### Stage: Remarketed
**Goal**: Shop rates across carriers, find best options

#### CX:
- Customer gets an update email: "We're shopping â update coming soon"
- They feel taken care of, not in the dark
- They think: "I don't have to do anything. They're handling it."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | 75 days out | Task: Submit | **"Submit {firstName}'s renewal to all eligible carriers. Log which carriers submitted to. Target: minimum 3 competing quotes."** | 15 min | Submitted |
| 2 | 60 days out | Task: Review quotes | **"Review returned quotes for {firstName}. Compare: premium, coverage, deductibles, carrier AM Best rating. Identify top 2-3 options. Note: Is there a savings vs. current? Any coverage improvements available?"** | 15 min | Options identified |
| 3 | 55 days out | Auto email | "We've been shopping your rates â update coming soon" | 0 min | Auto |
| 4 | 55 days out | Move to next stage | â Renewal Quoted | 0 min | Quotes ready |

---

### Stage: Renewal Quoted
**Goal**: Prepare and schedule renewal presentation

#### CX:
- Customer is invited to a quick renewal review â not just an auto-renewal notice
- They think: "They're actually going to walk me through my options? Most agents just send a bill."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | 50 days out | Task: Prepare presentation | **"Build renewal comparison for {First Name}. Show: Current policy vs. top 2-3 renewal options. Include: premium change ($X more/less), coverage changes, deductible options. Frame recommendations using Trust and Grow narrative: 'Here's our plan to keep you protected at the best value.'"** | 15 min | Comparison ready |
| 2 | 45 days out | Auto email | Scheduling link for renewal review call | 0 min | Auto |
| 3 | 40 days out | Reminder | **"Renewal review not yet scheduled for {firstName}. Text: 'Hey {firstName}, I've got your renewal options ready â it's a quick 10-minute call. Here's my link: [Link]' ** | 2 min | Review scheduled |

hedule renewal presentation

#### CX:
- Customer is invited to a quick renewal review â not just an auto-renewal notice
- They think: "They're actually going to walk me through my options? Most agents just send a bill."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | 50 days out | Task: Prepare presentation | **"Build renewal comparison for {First Name}. Show: Current policy vs. top 2-3 renewal options. Include: premium change ($X more/less), coverage changes, deductible options. Frame recommendations using Trust and Grow narrative: 'Here's our plan to keep you protected at the best value.'"** | 15 min | Comparison ready |
| 2 | 45 days out | Auto email | Scheduling link for renewal review call | 0 min | Auto |
| 3 | 40 days out | Reminder | **"Renewal review not yet scheduled for {firstName}. Text: 'Hey {firstName}, I've got your renewal options ready â it's a quick 10-minute call. Here's my link: [Link]' ** | 2 min | Review scheduled |

---

### Stage: Renewal Presented
**Goal**: Present options, get commitment

#### CX:
- Clear presentation of options â not confusing paperwork
- Empathetic handling of rate increases if applicable
- They think: "I understand my options. This agent fought to get me the best deal."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Review day | Task: Present | **"Conduct renewal review with {firstName}. Walk through comparison. If rate increased: acknowledge it, explain why (market, claims, inflation), show what you did to minimize it. If rate decreased: celebrate it. Either way, end with: 'Do you want to go ahead with this option, or take a day to think about it?' Don't push â confidence sells better than pressure."** | 15 min | Presentation delivered |
| 2 | 35 days out | Auto email | Recap + recommendation email | 0 min | Auto |
| 3 | 30 days out | Task: Follow-up | **"No decision yet from {First Name} on renewal. Text: 'Hey {First Name}, just checking in â did you have any questions about the renewal options? Happy to jump on a quick call. Your renewal date is {Date} so we have time, but I want to make sure you're set.'"** | 2 min | Decision made |

**Escalation**: 20 days to renewal with no decision â CSR manager alerted.

---

### Stage: Renewed
**Goal**: Confirm, celebrate, cross-sell, ask for referral

#### CX:
- Confirmation email: "You're renewed!"
- Cross-sell check: "While we're at it, let's make sure everything else is solid too"
- Referral request (they're at peak satisfaction)
- They think: "That was painless. I'm staying with this agency."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Immediate | Auto email | Renewal confirmation + thank you | 0 min | Auto |
| 2 | 7 days post | Auto email | Cross-sell check: "Your h·}e renewed â let's make sure your auto is in good shape too" | 0 min | Auto |
| 3 | 14 days post | Auto text | Referral ask: "Hey {firstName}, know anyone who could use an agent like us? We'd love to help your friends and family the same way." | 0 min | Auto |
| 4 | 14 days post | Task: Review | **"Post-renewal review for {First Name}. Check: 1) Policy renewed correctly in AMS. 2) Cross-sell opportunities noted. 3) Referral ask sent. 4) Any outstanding items? Close renewal cycle."** | 5 min | Renewal cycle closed |

---

### Stage: Lost to Competitor
**Goal**: Graceful exit, long-term win-back via Smart Cycle

#### CX:
- No guilt. No desperation. Class and dignity.
- They think: "If things don't work out with the new agent, I'm going back."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Immediate | Task: Log | **"Record reason for renewal loss: Price, Coverage, Service issue, Life change, Competitor offer, No response. Add notes. This feeds into monthly retention analysis."** | 2 min | Reason logged |
| 2 | 1 biz day | Auto email | Gracious farewell: "No hard feelings â I'm here if you ever need a second opinion." | 0 min | Auto |
| 3 | Immediate | Auto | Enroll in Smart Cycle for long-term win-back nurture | 0 min | Auto |

---

## Service Pipeline

### Stage: New Request
**Goal**: Acknowledge instantly, assign quickly, set expectations

#### CX:
- Immediate acknowledgment: "We got it, we're on it"
- They think: "I don't have to wonder if my message went into a black hole."

#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Immediate | Auto email/text | "Got your request, {firstName}. We're on it. You'll hear back within [timeframe]." | 0 min | Auto |
| 2 | Immediate | Task: Triage | **"New service request from {First Name}: [Request type]. 1) Read the request fully. 2) Is this something you can handle now? Do it. 3) Do you need carrier info? Note what you need and move to Waiting on Carrier. 4) Do you need client info? Note what you need and move to Waiting on Client. 5) Tesures target resolution: same day for simple requests, 48h for complex."** | 5 min | Triaged and either resolved or moved to correct stage |

### Stage: In Progress
#### CX: Client gets progress update within 24h if not resolved same-day.
#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | 24h | Reminder | **"Service request still open for {firstName}. Status update: text or email them with where things stand. Even 'Still working on this, expect an answer by [date]' is better than silence."** | 2 min | Update sent |

### Stage: Waiting on Carrier
#### CX: Client knows we're waiting on the carrier, not ignoring them.
#### EX: Carrier follow-up task every 48h. Escalation if no response in 5 business days.

### Stage: Waiting on Client
#### CX: Clear, simple request for what's needed. Easy to respond to.
#### EX: Follow-up reminder after 48h. Second reminder after 5 days. Resolve or close after 10 days with notice.

### Stage: Resolved
#### CX: Confirmation that it's handled + satisfaction check.
#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Immediate | Auto email | "All set!" [Brief summary of what was resolved]. Anything else I can help with?" | 0 min | Auto |
| 2 | 1 day | Task: Close | **"Close service request for {firstName}. Verify: resolution documented, AMS updated if needed, client confirmed satisfaction."** | 2 min | Closed |

---

## Claims Pipeline

**Claims are the moment of truth.** This is when the client discovers whether their agent is truly a guide or just a salesperson. Every CX touchpoint must radiate empathy and competence. Every EX task must be hyper-specific because the employee is dealing with a stressed client.

### Stage: Claim Reported
#### CX: Immediate empathy + clear guidance on what happens next.
#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Immediate | Task: First response | **"Claim reported by {First Name}. 1) Call them NOW ({Phone}). Say: 'I'm so sorry this happened. Let me help you through this â I'm going to walk you through exactly what to do.' 2) Gather: date of loss, description, photos if available. 3) File claim with {Carrier}. 4) Give them the claim number and adjuster timeline expectation. 5) Test them after the call: 'Here's your claim number: [X]. I'll follow up with you [tomorrow/this week]. Call me anytime if you need anything.'"** | 15 min | Claim filed, client informed |

### Stage: Adjuster Assigned
#### CX: Client receives adjuster info and knows what to expect.
#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Immediate | Task: Update client | **"Adjuster assigned for {First Name}'s claim. Send text/email: 'Your adjuster is [Name] at [Phone]. They'll reach out within [timeframe]. Here's what to expect: [brief overview of inspection/assessment process]. I'm monitoring this and will check in with you [day].' Log adjuster info in AZ."** | 5 min | Client informed |

### Stage: In Progress
#### CX: Weekly status update â never leave them wondering.
#### EX: Weekly task to call/text client with update. Even if no news: "Still in progress, I'm following up with the carrier this week."

### Stage: Settlement
#### CX: Agent reviews settlement WITH the client. Advocates if needed.
#### EX:

| Step | Timing | Type | Task Description | Time Est | Done When |
|------|--------|------|-----------------|----------|-----------|
| 1 | Immediate | Task: Review settlement | **"Settlement received for {First Name}'s claim. Amount: $[X]. 1) Review: Does this match what was expected? Is it fair? 2) If yes: call client, walk them through the settlement, explain what it covers. 3) If no/low: discuss with client whether to negotiate or accept. Advocate on their behalf if needed. 4) Document outcome."** | 15 min | Settlement reviewed with client |

### Stage: Closed
#### CX: Follow-up: "How was the experience? Anything else we can do?"
#### EX: Satisfaction check task. Cross-sell prevention check (make sure claim didn't create a coverage gap). Update AMS.

---

## Dream 100 Pipeline

### Stage: Identified
**CX**: N/A â research phase
**EX**: Complete prospect research card. Document: business type, estimated premium, mutual connections, relevant content to share, best channel to reach them.

### Stage: First Touch
**CX**: Personal, memorable introduction that provides value â not a cold pitch.
**EX**: Day 1 personalized email/note. Day 7 content piece. Day 14 text/social connection. All logged in AZ.

### Stage: Engaged
**CX**: Bi-weekly value delivery. They think: "This person keeps showing up with useful stuff."
**EX**: Task every 2 weeks with specific touchpoint instructions. Vary channels: email, text, social, in-person, mail.

### Stage: Meeting Set â Relationship Active â Converted
**CX**: Genuine relationship building, not a pipeline push.
**EX**: Pre-meeting prep task with agenda + content. Post-meeting follow-up within 24h. Monthly relationship maintenance task.
