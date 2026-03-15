# Day 1 - System Design

**System Design:** URL Shortener

**Tasks to complete:**
- [ ] Define functional requirements: redirect, create short URL, custom aliases
- [ ] Define non-functional requirements: high availability, low latency, redirect speed
- [ ] Design database schema: URL table with original_url, short_code, click_count, created_at
- [ ] Design API endpoints: POST /shorten, GET /{short_code}, GET /{short_code}/stats
- [ ] Discuss hash function choices: base-62 encoding vs random ID
- [ ] Analyze read vs write ratio implications