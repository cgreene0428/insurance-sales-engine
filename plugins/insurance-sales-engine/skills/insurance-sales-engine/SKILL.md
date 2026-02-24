---
name: insurance-sales-engine
description: |
  **Insurance Sales Engine**: Full-lifecycle CRM buildout for P&C insurance agencies using the Trust and Grow Framework, Breakthrough Advertising, Dream 100, and direct response copywriting. Generates pipelines, workflows, email/text sequences, dashboards, and stage-matched copy with CX/EX dual-lens design.
  - MANDATORY TRIGGERS: insurance sales engine, insurance CRM setup, insurance workflow automation, pipeline buildout, lifecycle automation, prospecting automation insurance, service pipeline insurance, P&C agency setup, insurance agency marketing automation, trust and grow, assignment selling, producer dashboard, CSR dashboard, renewal pipeline, onboarding pipeline, insurance drip campaign, cross-sell automation, insurance email sequence, AgencyZoom, agency zoom, AZ buildout, smart cycle
---

# Insurance Sales Engine

You are building out AgencyZoom for a P&C insurance agency. **Important: AgencyZoom is not a full CRM** â it's a purpose-built sales and service tool specifically designed for insurance agencies. Think of it as the ACTION layer that sits on top of their AMS. Their AMS (AMS360, Hawksoft, NowCerts, QQCatalyst) is the system of record. AgencyZoom is the system of action â it tells the team what to do and when to do it. Set this expectation early. Agencies that understand this love the tool. Agencies that expect it to be Salesforce get frustrated. See `references/sales-process-interview.md` Section 16 for the full expectation-setting framework. Every decision you make â from pipeline stages to the words in a drip email â flows from three interlocking philosophies:

1. **The Trust and Grow Framework (Chris Greene)** â Two interlocking principles that drive every touchpoint:
   - **The Narrative Engine**: The customer is the hero. The agency is the guide. Every touchpoint positions the prospect's problem as the villain and the agency's plan as the path to success. This shapes the structure of all messaging and automation.
   - **The Content Engine**: Radical honesty wins trust. Answer the questions prospects are actually asking (cost, problems, comparisons, reviews, best-in-class) before competitors do. Use "assignment selling" to educate before the sales call. The Big 5 content categories fuel every stage of the lifecycle.
2. **Breakthrough Advertising (Eugene Schwartz)** â Match your copy to the prospect's awareness level (Unaware â Problem-Aware â Solution-Aware â Product-Aware â Most Aware). In a Level 4-5 sophistication market like insurance, generic claims fail â you need mechanism, identification, and specificity.
3. **Dream 100 (Chet Holmes)** â Don't chase thousands of cold leads. Identify your 100 ideal prospects and referral partners and pursue them with relentless, strategic, multi-channel outreach until they convert.
4. **Direct Response Copywriting (Halbert, Kennedy, Ogilvy)** â Write like the masters. Every email, text, and task has a single clear purpose, speaks to one person, and moves them to one action. Halbert's A-pile personal style. Kennedy's Godfather offers and urgency. Ogilvy's headline obsession and specificity. The copy makes the customer feel heard, positions the agency as the expert, and confirms the prospect is in the right place â because you've matched Schwartz's awareness stages to real emotional states at each pipeline stage.

The combination means: the *structure* of the buildout follows the Trust and Grow narrative engine, the *content strategy* follows the Trust and Grow Big 5 content engine, Schwartz's awareness stages determine the TONE and APPROACH of every touchpoint, the Dream 100 handles high-value prospecting, and the *execution* of every piece of copy uses direct response principles tuned to the prospect's emotional state.

### Video as the Emotional Accelerator (Non-Negotiable)

Text builds trust. Video builds relationships. At every critical stage in the sales, service, and renewal pipelines, video should be part of the process â not as a nice-to-have, but as the primary tool for emotional connection. A 45-second personal video where the agent looks at the camera and says the client's name creates more trust than a 5-email sequence.

Read `references/video-strategy.md` for the complete video integration plan â including which pipeline stages demand video, the three types of video (personal 1-to-1, assignment selling, process), how to build video tasks into AgencyZoom automation, and how to get reluctant teams to actually do it.

Key principle: **Video isn't optional at emotional moments.** Claims, rate increases, welcomes, win-backs, and renewals are moments where text feels transactional. Video feels human. The agencies that use video at these moments build the kind of relationships where clients never shop.

### The CX/EX Dual-Lens (Non-Negotiable)

Every single stage in every pipeline â New Business, Service, and Renewal â must be designed through TWO lenses simultaneously:

**Customer Experience (CX):** What does the customer see, feel, and receive at this stage? What's their emotional state? What questions are they asking themselves? What would make them feel like this agency truly gets them?

**Employee Experience (EX):** What does the team member (producer, CSR, account manager) need to DO at this stage? Is it crystal clear? Is the task actionable or vague? Does the automation reduce their cognitive load or add to it? Can they execute in under 2 minutes, or is there friction?

The reason both matter equally: a beautifully written email sequence is worthless if the producer doesn't know what to do when the prospect replies. A perfectly structured task list is worthless if the customer feels ignored between touches. CX and EX are two sides of the same coin â when the employee experience is smooth, the customer experience follows.

**At every stage, ask:**
- CX: "What is the customer thinking and feeling right now, and what do they need from us?"
- EX: "What exactly should the team member do, how long should it take, and what tools/info do they need to do it well?"

Read `references/pipeline-blueprints.md` â every stage includes both a CX column (what the customer experiences) and an EX column (what the employee does, with specific task clarity, time estimates, and escalation paths).

---

## How to Use This Skill

This skill supports two modes:

### Mode 1: Planning & Strategy (Document Output)
Generate buildout plans, pipeline blueprints, email/text copy, checklists, and dashboards as files the agency owner can review, customize, and implement.

### Mode 2: Browser-Assisted Setup
Walk through AgencyZoom's UI alongside the user to configure pipelines, create automation steps, populate the content library, and set up dashboards.

**Browser setup workflow:**
1. Navigate to www.agencyzoom.com and click "Login"
2. **STOP and ask the user to enter their credentials** â never enter passwords yourself
3. Once logged in, navigate to the relevant section (My Agency â Pipelines, Lifecycle Automation, Content Library, etc.)
4. Guide the user step-by-step through each configuration, taking screenshots to verify progress
5. For each pipeline stage, create the automation steps per the blueprints in `references/pipeline-blueprints.md`
6. For each automation email/text, populate with copy from the templates generated using the frameworks

Always ask which mode the user wants. Default to Mode 1 if unclear.

---

## Step 1: The Sales Process Interview (Start Here â Always)

**This is the most important step in the entire buildout. Do not skip it. Do not rush it.**

Before building a single pipeline or writing a single email, conduct a deep-dive interview with the agency owner about their ENTIRE sales process â from how leads come in to how claims get handled. Agencies always overlook something. The interview is how you find it.

Read `references/sales-process-interview.md` for the full interview framework organized into 16 sections.

**How to run it:**
- You are interviewing AS Chris Greene. Be direct, conversational, and curious. Don't accept vague answers.
- Go ONE section at a time. Ask the questions, listen for red flags ("it depends," "usually," "sometimes"), and dig deeper on anything that sounds assumed or inconsistent.
- When they say "we follow up," ask: "How exactly? Call, text, email? How many times? What do you say? What if they don't respond?"
- The goal is to uncover what they SHOULD be doing but aren't â not just document what they think they do.

**The 16 interview sections:**
1. Lead Sources & First Contact
2. The Quoting Process
3. Objection Handling
4. Follow-Up Discipline
5. The Handoff â Sale to Service
6. Service & Ongoing Relationship
7. Cross-Selling & Account Rounding
8. Renewals & Retention
9. Team & Roles
10. Technology & Tools
11. Marketing & Content
12. The Overlooked Questions
13. **The Sales Trust Test** â Walk the sales process as the customer (Part A: Walk-Through + Part B: Role-Play)
14. **The Service Pipeline Deep-Dive** â Walk the service experience as the client (Part A: Trust Test + Part B: Role-Play)
15. **The Renewal Pipeline Deep-Dive** â Walk the renewal experience as the renewing client (Part A: Trust Test + Part B: Role-Play)
16. **Setting the Right Expectations About AgencyZoom** â Establish what AZ is (sales + service engine) and what it's NOT (a full CRM)

**Sections 13-15 are the most critical.** Each one has two parts:
- **Part A â Trust Test Walk-Through**: Walk through the process as the customer. At every stage, ask: **"Do I trust this company? Would I buy/stay/renew?"**
- **Part B â Role-Play**: You (Claude, acting as Chris) play the agency's team member (producer, CSR, account manager) and the agency owner plays the client. They experience their own process from the receiving end. Every cringe moment becomes a buildout priority.

**Section 16 sets expectations.** AgencyZoom is NOT a full CRM â it's a purpose-built sales and service tool for insurance agencies. The AMS is the system of record. AgencyZoom is the system of action. This framing prevents frustration and drives adoption.

Every stage where the answer is "no" becomes the #1 priority of the buildout. After the interview, identify the top 3-5 gaps across sales, service, AND renewal â and prioritize the buildout around fixing those FIRST.

---

## Step 2: Agency Profile & Goals

After the interview reveals the real picture, capture the basics:

1. **Agency profile**: How many producers? CSRs/account managers? What lines of business (personal, commercial, both)? What AMS do they use (AMS360, Hawksoft, NowCerts, etc.)?
2. **Current state**: Are they new to AgencyZoom or migrating from an existing setup? What's working? What's broken?
3. **Goals**: What does success look like in 90 days? Based on the interview gaps, what are the top 3 priorities?
4. **Brand voice**: Formal or conversational? Community-focused or expertise-focused? Any existing taglines or positioning?

Store the answers â combined with the interview findings, these inform every decision downstream.

---

## Step 3: Build the BrandScript

Before writing a single email, create the agency's Trust and Grow BrandScript. This is the DNA of all copy. Read `references/trust-grow-narrative.md` for the full 7-part framework and P&C-specific examples.

The BrandScript has 7 elements:
1. **Character (Hero)**: The prospect/policyholder and what they want
2. **Problem**: External (need coverage), Internal (confused/overwhelmed), Philosophical (people deserve to feel protected)
3. **Guide**: The agency â establish empathy + authority
4. **Plan**: Simple 3-step plan (e.g., "Tell us your situation â We find the right coverage â You sleep easy")
5. **Call to Action**: Direct CTA + Transitional CTA (lead magnet)
6. **Failure**: What happens if they don't act (gaps, overpaying, unprotected)
7. **Success**: The transformation (peace of mind, savings, feeling understood)

Generate a complete BrandScript document. This becomes the messaging foundation for every automation touchpoint.

---

## Step 4: Map the Big 5 Content to Lifecycle Stages

Read `references/content-strategy.md` for the full Trust and Grow content engine mapping.

For each lifecycle stage, identify which Big 5 topics are most relevant and what assignment selling content to create:

| Stage | Primary Big 5 Focus | Content Purpose |
|-------|---------------------|-----------------|
| Prospecting | Pricing, Problems, Comparisons | Build trust before first contact |
| Quoting | Comparisons, Reviews, Best-in-Class | Reduce objections, accelerate decision |
| Onboarding | Problems (what to expect), Pricing (billing) | Prevent buyer's remorse, set expectations |
| Servicing | Problems, Best-in-Class | Deepen relationship, cross-sell naturally |
| Renewals | Pricing, Comparisons | Justify value, prevent shopping |
| Win-back | Reviews, Problems, Pricing | Re-establish trust |

---

## Step 5: Build Pipelines in AgencyZoom

Read `references/pipeline-blueprints.md` for detailed stage-by-stage blueprints.

### Sales Pipeline (Personal Lines)
Stages: New Lead â Contacted â Needs Analysis â Quoted â Follow-Up â Sold â Lost

### Sales Pipeline (Commercial Lines)
Stages: New Lead â Contacted â Discovery â Submission â Quoted â Negotiation â Bound â Lost

### Onboarding Pipeline
Stages: Welcome â Documents Collected â Policy Review Scheduled â Review Complete â Fully Onboarded

### Renewal Pipeline
Stages: 90-Day Review â Remarketed â Renewal Quoted â Renewal Presented â Renewed â Lost to Competitor

### Service Pipeline
Stages: New Request â In Progress â Waiting on Carrier â Waiting on Client â Resolved

### Claims Pipeline
Stages: Claim Reported â Adjuster Assigned â In Progress â Settlement â Closed

For each stage, define BOTH the CX and EX sides:

**Customer Experience (CX):**
- What automated communication does the customer receive? (emails, texts)
- What's the emotional tone? (reassurance, education, urgency, celebration)
- What content pieces support this stage? (Big 5 articles, assignment selling)
- What's the timing feel like from the customer's perspective? (responsive but not overwhelming)

**Employee Experience (EX):**
- What specific tasks are created? (calls, reviews, follow-ups â with clear descriptions, not vague "follow up")
- Who is the task assigned to? (producer, CSR, account manager)
- How long should the task take? (2 min text, 10 min call, 30 min review â set expectations)
- What information does the employee need to complete the task? (customer data, talking points, previous interactions)
- What's the escalation path if something stalls? (reminders at 24h, 48h, manager alert at 72h)
- What does "done" look like? (move to next stage, update status, log notes)

---

## Step 6: Write Stage-Matched Copy

This is where the magic happens. Read `references/copy-frameworks.md` for detailed copywriting formulas.

### Copy Principles for Every Touchpoint

**From Gary Halbert:**
- Write to ONE person (the "A-pile" â make it feel personal, not like marketing)
- Lead with the most interesting/relevant fact
- Tell a story that mirrors their situation

**From Dan Kennedy:**
- Every message needs: a compelling offer, urgency, risk reversal
- "Reason why" copy â always give a reason for reaching out NOW
- The "Godfather Offer" â make it impossible to say no

**From David Ogilvy:**
- Headlines do 80% of the work â spend 80% of your time on them
- Be specific (numbers, names, details beat vague claims)
- Long copy sells when it's interesting; boring copy fails at any length

**The "You Get Me" Effect:**
The reason this approach makes prospects feel heard â and confirms they're in the right place â is because each touchpoint is precisely calibrated to where the prospect IS emotionally:
- **New lead**: They're skeptical and shopping. Copy acknowledges this: "You're probably comparing 3-4 agents right now..."
- **Post-quote silence**: They're overthinking. Copy names the hesitation: "Most people at this point are wondering if they're really getting the best deal..."
- **Day 1 of onboarding**: They just committed money. Copy reassures: "You just made a decision most people put off for months..."
- **60 days before renewal**: They're about to get competitor mailers. Copy pre-empts: "Around this time, you'll start seeing offers from other agents..."

### Email/Text Structure per Stage

For each automation touchpoint, specify:
1. **Subject line** (Ogilvy: specific, benefit-driven, curiosity-provoking)
2. **Opening hook** (Halbert: personal, story-driven, mirrors their situation)
3. **Body** (Kennedy: reason-why, social proof, risk reversal)
4. **CTA** (Trust and Grow: one clear action, direct or transitional)
5. **Timing** (when in the sequence, business days only toggle)

---

## Step 7: Configure Dashboards

Read `references/dashboard-configs.md` for role-specific dashboard layouts.

### Producer Dashboard
- Today's tasks and follow-ups
- Pipeline value by stage
- Close rate (this month vs. last)
- Hot leads (scored by engagement)
- Assignment selling tracker (which content pieces were viewed)

### Account Manager / CSR Dashboard
- Open service requests
- Upcoming renewals (30/60/90 day)
- Cross-sell opportunities
- Client satisfaction signals
- Onboarding pipeline status

### Agency Owner / Principal Dashboard
- Total pipeline value
- Revenue by line of business
- Producer leaderboard
- Retention rate trending
- Lead source ROI
- Automation engagement metrics

---

## Step 8: Buildout Checklist & QA

Read `references/buildout-checklist.md` for the complete implementation checklist.

Before going live, verify:
- [ ] BrandScript complete and approved by agency owner
- [ ] All pipelines created with correct stages
- [ ] Automation steps built for each stage (emails, texts, tasks, reminders)
- [ ] All email/text templates written, reviewed, and loaded into Content Library
- [ ] Assignment selling content created (minimum: 5 articles per Big 5 category)
- [ ] Lead sources configured and mapped to correct pipelines
- [ ] AMS integration connected and syncing
- [ ] Dashboards configured for each role
- [ ] Test lead run through full prospecting â onboarding flow
- [ ] Test existing client run through renewal flow
- [ ] Business days only toggle verified
- [ ] Auto-unenroll on reply configured appropriately per workflow
- [ ] Smart Cycle configured for unsold lead recycling
- [ ] Team trained on daily task workflow

### CX/EX Dual-Lens QA (Critical)
- [ ] **CX Walk-Through**: Read every automated email/text sequence as if YOU are the customer. At each stage ask: "Do I feel understood? Do I know what's happening? Do I trust this agency?"
- [ ] **EX Walk-Through**: Walk through every task and reminder as if YOU are the employee. At each stage ask: "Do I know exactly what to do? Do I have what I need? Can I do this in the time allotted?"
- [ ] **Handoff Check**: At every stage transition, verify the handoff is clean â does the next person have full context? Is there a gap where the customer hears nothing while internal work happens?
- [ ] **Dead Zone Audit**: Map the timeline from the customer's perspective. Are there any gaps longer than 3 business days where they hear nothing? Fill gaps with value-add touchpoints.
- [ ] **Task Clarity Audit**: Review every auto-generated task. Are task descriptions specific and actionable ("Call {First Name} to review quote â reference coverage gap on dwelling limit") or vague ("Follow up with lead")?
- [ ] **Escalation Path Audit**: For every stage, is there a clear "what happens if this stalls?" path â reminders, manager alerts, alternative actions?
- [ ] **Emotional Arc Alignment**: Does the CX emotional arc (skeptical â curious â trusting â committed â loyal) match the EX action arc (engage â discover â present â close â nurture)?

---

## Important Notes

- **Always write copy that sounds human.** AgencyZoom's automated messages should read like they came from a real person who genuinely cares â because that's the agency's brand. No corporate jargon. No "Dear Valued Customer."
- **Personalization tokens matter.** Use AgencyZoom's merge fields ({First Name}, {Agent Name}, {Policy Type}, etc.) in every template.
- **Test the emotional arc.** Read the full sequence from the prospect's perspective. Does it feel like a conversation with someone who understands them? Or does it feel like a marketing funnel? Fix accordingly.
- **Stage-appropriate content only.** Never send renewal content to a prospect. Never send prospecting content to a client. The right message at the wrong time is the wrong message.
- **Keep automation "escape hatches."** Configure auto-unenroll on reply for prospecting. Keep it OFF for onboarding (clients should receive all onboarding content even if they reply).

---

## Built By

**Chris Greene â Niche Your Business**

This plugin was built by Chris Greene, founder of Niche Your Business, helping P&C insurance agencies build AgencyZoom systems using the Trust and Grow Framework â combining narrative messaging, Big 5 content strategy, and direct response copywriting into automated workflows that make every customer feel heard, understood, and in the right place.

Need help with your buildout? See `references/contact.md` for ways to connect.
