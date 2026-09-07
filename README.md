# EstateFlow

A polished prototype for estate/community operations — resident CRM, house registry, service-charge collections, M-Pesa reconciliation, vendor expenses, committee workflows and communications.

## Prototype scope
- One-page public landing/login experience
- Role-aware navigation for Chairperson, Treasurer, Secretary, Estate Manager, Security Lead and Resident
- Estate/house CRM with resident contacts and charge status
- Service-charge billing and arrears views
- M-Pesa-ready reconciliation queue for inflows and outflows
- Vendor/service management for security, garbage, landscaping and water
- Expense approval workflow: request → review → approve → pay → reconcile
- Notices, meetings/minutes, reports and settings shells
- Responsive mobile/tablet/desktop UI

## Production architecture to add
1. **Authentication & RBAC:** Supabase/Auth.js/Clerk with server-side route protection and permissions matrix.
2. **Database:** Postgres entities for estates, blocks, houses, residents, occupancy, charges, invoices, payments, M-Pesa transactions, vendors, expenses, approvals, services, notices, meetings and audit logs.
3. **M-Pesa:** Safaricom Daraja STK Push + C2B/B2C where appropriate, callback validation, immutable transaction IDs, idempotency and automated matching rules. Never trust client-side payment status.
4. **Reconciliation:** Match by account/Paybill, phone, amount, reference, timestamp and house/member mapping; send exceptions to a review queue.
5. **Money controls:** maker/checker approval, configurable spending limits, dual approval for high-value payments, attachment/evidence requirements and complete audit trail.
6. **Notifications:** SMS/email/WhatsApp provider integration for receipts, arrears reminders, approvals, notices and security alerts.
7. **Reporting:** monthly income/expense, arrears ageing, vendor spend, service performance, cash/bank/M-Pesa reconciliation and downloadable statements.

## Important product gaps to cover before production
- Owner vs tenant vs caretaker relationships and multiple occupants per house
- House/parking/store/unit allocation and occupancy history
- Move-in/move-out records and deposit tracking
- Meter readings/utilities where the estate needs them
- Incident/security log and visitor/access management
- Maintenance requests with SLA, photos, assignment and status history
- Vendor contracts, renewal dates, invoices and compliance documents
- Procurement/quotation comparison before large purchases
- Budget vs actual by service/category
- Committee elections, term dates and delegated authority
- Conflict-of-interest declarations
- Document vault and meeting minutes
- Resident complaints/disputes and escalation workflow
- Emergency contacts and broadcast alerts
- Data privacy, retention, backups, export and deletion policies
- Full immutable audit log for financial/admin actions

## Brand direction
**Name:** EstateFlow — Community OS

**Palette:** Deep Forest `#12392B`, Estate Green `#1F6B4D`, Mint `#DCEEE3`, Warm Gold `#CAA55B`, Paper `#F7F8F5`, Ink `#18231E`.

The design intentionally feels like premium fintech + modern property management rather than a traditional estate committee spreadsheet.
