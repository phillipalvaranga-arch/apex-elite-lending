EMAIL='contact@apexelitelending.com'
TODO='<span class="todo">TODO: confirm email</span>'
DISC='Business-purpose loans only. Not a consumer lender at this time.'
NAV=[('index.html','Home'),('business-loans.html','Business Loans'),('personal-loans.html','Personal Loans'),('about.html','About'),('faq.html','FAQ'),('contact.html','Contact')]
def page(fn,title,desc,body):
    links=''.join(f'<a href="{h}"{" class=on" if h==fn else ""}>{t}</a>' for h,t in NAV)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Apex Elite Lending LLC</title><meta name="description" content="{desc}"><meta name="theme-color" content="#0a1628">
<link rel="icon" href="favicon.png"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="stylesheet" href="style.css"></head><body>
<header><div class="wrap nav"><a class="brand" href="index.html"><img src="logo.png" alt="Apex Elite logo" width="40" height="40">Apex Elite <span>Lending</span></a>
<button id="mt" aria-label="Menu" onclick="document.querySelector('nav.links').classList.toggle('open')">☰</button>
<nav class="links">{links}<a class="btn" href="apply.html">Apply</a></nav></div></header>
<main>{body}</main>
<footer><div class="wrap"><div class="fgrid"><div><a class="brand" href="index.html" style="display:flex"><img src="logo.png" alt="" width="32" height="32">Apex Elite <span>Lending</span> LLC</a>
<p>Small business-purpose loans for Texas entrepreneurs. Based in Frisco, Texas.</p><p>Email: <a style="display:inline" href="mailto:{EMAIL}">{EMAIL}</a> {TODO}</p></div>
<div><b>Company</b>{''.join(f'<a href="{h}">{t}</a>' for h,t in NAV)}</div><div><b>Get started</b><a href="apply.html">Apply</a><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a></div></div>
<div class="disc"><b>{DISC}</b> Personal loans are coming soon, pending Texas licensing; Apex Elite Lending LLC does not currently offer, make, or arrange consumer loans. All loans are subject to application, review, and approval. Rates shown are maximums and examples, not offers. © 2026 Apex Elite Lending LLC, Frisco, Texas.</div></div></footer>
</body></html>'''
P={}
P['index.html']=('Small Business Loans in Frisco, Texas','Apex Elite Lending offers small business-purpose loans of $1,000 to $2,500 at no more than 18% APR.',f'''
<section class="hero"><div class="wrap"><span class="pill">Frisco, Texas · Business-purpose loans</span>
<h1>Small business funding,<br><em>handled personally.</em></h1>
<p>Apex Elite Lending provides business-purpose loans of <b>$1,000 to $2,500</b> to Texas small businesses, with a maximum rate of <b>18% APR</b>, simple fixed payments, and no hidden fees.</p>
<p style="margin-top:28px"><a class="btn" href="apply.html">Start your application</a> &nbsp; <a class="btn ghost" href="business-loans.html">See loan details</a></p></div></section>
<section class="alt"><div class="wrap"><h2>How it works</h2><p class="lead">Straightforward steps, with a real person on the other end.</p>
<div class="grid"><div class="card"><div class="num">1</div><h3>Send an inquiry</h3><p>Tell us about your business, how much you need, and what it's for. It takes a few minutes and asks for no sensitive information.</p></div>
<div class="card"><div class="num">2</div><h3>Review together</h3><p>We follow up to discuss your needs and securely collect the documents needed for a review, such as business bank statements.</p></div>
<div class="card"><div class="num">3</div><h3>Decision & terms</h3><p>If approved, you get clear written terms: amount, rate, payment, and schedule, before you sign anything.</p></div>
<div class="card"><div class="num">4</div><h3>Get funded</h3><p>Funds are sent to your business account, and you repay in fixed monthly installments.</p></div></div></div></section>
<section><div class="wrap"><h2>Why Apex Elite</h2><div class="grid">
<div class="card"><h3>Built for small amounts</h3><p>Many lenders won't bother with small loans. We focus on the $1,000 to $2,500 range that helps a small business cover equipment, inventory, or a cash-flow gap.</p></div>
<div class="card"><h3>Capped, transparent pricing</h3><p>Our rates never exceed 18% APR, within Texas limits for business loans. You'll see every cost in writing up front.</p></div>
<div class="card"><h3>Local & personal</h3><p>We're a Frisco-based company. You'll deal directly with the people making decisions, not a call center.</p></div>
<div class="card"><h3>Fair & consistent</h3><p>Every application is reviewed against the same written criteria. We never promise "guaranteed approval."</p></div></div>
<div class="notice">{DISC} Personal loans are <a href="personal-loans.html">coming soon, pending Texas licensing</a>.</div></div></section>''')
P['business-loans.html']=('Business Loans','Business-purpose loans from $1,000 to $2,500, maximum 18% APR, with an example payment calculator.',f'''
<div class="page-h"><div class="wrap"><h1>Business Loans</h1><p>Small, straightforward funding for Texas businesses.</p></div></div>
<section><div class="wrap"><div class="grid"><div class="card"><h3>Loan amounts</h3><p class="out">$1,000 to $2,500</p><p class="note">First-time borrowers may be offered a smaller amount. Repeat borrowers in good standing may qualify for more over time.</p></div>
<div class="card"><h3>Rate</h3><p class="out">Up to 18% APR</p><p class="note">Fixed rate, never above 18% APR. Your actual rate depends on our review.</p></div>
<div class="card"><h3>Terms</h3><p class="out">Fixed monthly payments</p><p class="note">Term lengths are set case by case and shown in your written loan agreement before you sign.</p></div></div>
<h2 style="margin-top:50px">Common uses</h2><ul class="check"><li>Equipment and tools</li><li>Inventory and supplies</li><li>Short-term cash-flow gaps</li><li>Marketing, licenses, or small upgrades</li></ul></div></section>
<section class="alt" id="calculator"><div class="wrap"><h2>Example payment calculator</h2><p class="lead">Estimate a fixed monthly payment. This is an illustration only, not an offer or a quote.</p>
<div class="card" style="max-width:640px"><div class="row2"><div><label for="amt">Loan amount ($)</label><input id="amt" type="number" min="1000" max="2500" step="100" value="2000"></div>
<div><label for="apr">APR (%)</label><input id="apr" type="number" min="0" max="18" step="0.5" value="18"></div></div>
<label for="term">Term (months)</label><select id="term"><option>3</option><option>6</option><option selected>12</option><option>18</option><option>24</option></select>
<p style="margin-top:20px">Estimated monthly payment</p><p class="out" id="pay">-</p><p id="tot" class="note"></p>
<p class="note">Assumes equal monthly payments and simple interest, with no fees. Amounts are limited to $1,000 to $2,500 and APR to 18%. Actual terms, APR, and payments are in your written agreement and may differ.</p></div>
<script>
function calc(){{let a=Math.min(2500,Math.max(1000,+amt.value||0)),r=Math.min(18,Math.max(0,+apr.value||0))/1200,n=+term.value;
let p=r?a*r/(1-Math.pow(1+r,-n)):a/n;pay.textContent='$'+p.toFixed(2);tot.textContent=`${{n}} payments · total repaid $${{(p*n).toFixed(2)}} · total interest $${{(p*n-a).toFixed(2)}} (on $${{a.toLocaleString()}})`}}
['amt','apr','term'].forEach(i=>document.getElementById(i).addEventListener('input',calc));calc();</script></div></section>
<section><div class="wrap"><h2>Typical requirements</h2><p class="lead">Examples of what we generally look for. We'll tell you exactly what's needed for your application.</p>
<ul class="check"><li>A Texas-based business, generally operating 12+ months (6+ months may be considered with strong owner credit)</li>
<li>An EIN or assumed-name (DBA) certificate</li><li>3 to 6 months of business bank statements, with deposits that comfortably support the payment</li>
<li>Valid government ID for each owner, plus identity verification</li><li>A credit review, done only with your signed consent</li>
<li>A personal guaranty from owners of 20% or more, and a signed business-purpose certification</li><li>A clear, legitimate business use for the funds</li></ul>
<p class="note">We do not lend to illegal businesses, for gambling, or to refinance other lenders or merchant cash advances. Approval is not guaranteed.</p>
<p><a class="btn" href="apply.html">Apply now</a></p><div class="notice">{DISC}</div></div></section>''')
P['personal-loans.html']=('Personal Loans: Coming Soon','Personal loans from Apex Elite Lending are coming soon, pending Texas licensing.',f'''
<div class="page-h"><div class="wrap"><span class="pill">Coming soon</span><h1>Personal Loans</h1><p>Pending Texas licensing.</p></div></div>
<section><div class="wrap" style="max-width:780px"><p>Apex Elite Lending plans to offer small personal installment loans in the future. <b>We are not licensed to make consumer loans yet, and we do not currently offer, make, or arrange personal, family, or household loans.</b> We'll announce here when that changes.</p>
<div class="notice"><b>Want to know when personal loans are available?</b><br>Email <a href="mailto:{EMAIL}?subject=Personal%20loans%20-%20notify%20me&body=Please%20let%20me%20know%20when%20personal%20loans%20become%20available.">{EMAIL}</a> {TODO} with the subject "Notify me." Joining the interest list is not an application and is not a commitment to lend.</div>
<p>If you need funding for a <b>business purpose</b>, see our <a href="business-loans.html">business loans</a>.</p><p class="note">{DISC}</p></div></section>''')
P['about.html']=('About Us','About Apex Elite Lending LLC, a small business lender based in Frisco, Texas.',f'''
<div class="page-h"><div class="wrap"><h1>About Apex Elite Lending</h1><p>A Frisco, Texas company focused on small business funding.</p></div></div>
<section><div class="wrap" style="max-width:820px"><p>Apex Elite Lending LLC is a new, independently owned lending company based in Frisco, Texas. We started with a simple idea: small businesses sometimes need a small amount of capital, and they deserve a lender who treats a $1,500 request as seriously as a large one.</p>
<p>We're starting deliberately small, making business-purpose loans of $1,000 to $2,500 at no more than 18% APR, so we can serve each borrower personally and build a track record the right way.</p>
<h2 style="margin-top:36px">Our commitments</h2><ul class="check"><li><b>Transparency:</b> every cost and payment in writing before you sign.</li><li><b>Fairness:</b> the same written criteria for every applicant, in line with fair-lending laws.</li><li><b>Respect:</b> professional, lawful communication at every stage, including collections.</li><li><b>Privacy:</b> we collect only what we need and protect it carefully.</li><li><b>Honesty:</b> no "guaranteed approval," no hidden fees, no pressure.</li></ul>
<h2 style="margin-top:36px">What's next</h2><p>As the company grows, we intend to apply for Texas licensing to offer personal installment loans. Until then, <b>we offer business-purpose loans only.</b></p><p><a class="btn" href="contact.html">Get in touch</a></p></div></section>''')
faq=[('Who can apply?','Texas small businesses and business owners who need funds for a business purpose, such as equipment, inventory, or cash flow.'),
('How much can I borrow?','Business-purpose loans currently range from $1,000 to $2,500. First-time borrowers may be offered a smaller amount.'),
('What is the interest rate?','Rates are fixed and never exceed 18% APR. Your rate depends on our review and appears in your written agreement before you sign.'),
('Do you offer personal loans?','Not yet. Personal loans are coming soon, pending Texas licensing. We currently make business-purpose loans only and are not a consumer lender at this time.'),
('Can I use a business loan for personal expenses?',"No. Loans must be used primarily for business purposes, and you'll sign a business-purpose certification."),
('Do you check credit?','We may review credit as part of underwriting, only with your signed consent. A credit history alone doesn\'t decide an application.'),
('Is approval guaranteed?','No. Every application is reviewed against the same written criteria, and approval is never guaranteed.'),
('Why doesn\'t the online form ask for my SSN or bank details?',"To protect you. The website form only starts the conversation. If we move forward, we'll collect any sensitive documents through a secure method, never by regular email or website form."),
('How do I repay?','Through fixed monthly payments on a set schedule. Automatic payments may be available with your written authorization, which you can revoke.'),
('Are there prepayment penalties?','Prepayment terms will be stated in your loan agreement. Ask us before you apply.')]
P['faq.html']=('FAQ','Frequently asked questions about Apex Elite Lending business loans.','<div class="page-h"><div class="wrap"><h1>Frequently Asked Questions</h1></div></div><section><div class="wrap" style="max-width:820px">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)+'<p style="margin-top:30px">Still have a question? <a href="contact.html">Contact us</a>.</p></div></section>')
P['contact.html']=('Contact','Contact Apex Elite Lending LLC in Frisco, Texas.',f'''
<div class="page-h"><div class="wrap"><h1>Contact Us</h1><p>We'd love to hear about your business.</p></div></div>
<section><div class="wrap"><div class="grid"><div class="card"><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a><br>{TODO}</p></div>
<div class="card"><h3>Phone</h3><p><span class="todo">TODO: add business phone</span></p></div>
<div class="card"><h3>Location</h3><p>Frisco, Texas<br><span class="todo">TODO: add mailing address if desired</span></p></div></div>
<div class="notice">Please don't email Social Security numbers, bank account numbers, or other sensitive information. We'll arrange a secure way to collect documents if needed.</div>
<p><a class="btn" href="apply.html">Start an application</a></p></div></section>''')
P['apply.html']=('Apply','Start a business-purpose loan inquiry with Apex Elite Lending.',f'''
<div class="page-h"><div class="wrap"><h1>Apply for a Business Loan</h1><p>Start with a quick inquiry. We'll follow up personally.</p></div></div>
<section><div class="wrap" style="max-width:760px"><div class="notice"><b>Do not include sensitive information.</b> This form never asks for your Social Security number, bank account details, or ID numbers. When you press Send, it opens a prefilled email in your own mail app addressed to {EMAIL} {TODO}. Nothing is stored on this website.</div>
<form class="card" id="f"><div class="row2"><div><label for="name">Full name *</label><input id="name" required autocomplete="name"></div><div><label for="biz">Business name *</label><input id="biz" required autocomplete="organization"></div>
<div><label for="em">Email *</label><input id="em" type="email" required autocomplete="email"></div><div><label for="ph">Phone</label><input id="ph" type="tel" autocomplete="tel"></div></div>
<label for="amt">Amount requested *</label><select id="amt" required><option value="">Select…</option><option>$1,000</option><option>$1,500</option><option>$2,000</option><option>$2,500</option></select>
<label for="pur">Business purpose *</label><select id="pur" required><option value="">Select…</option><option>Equipment / tools</option><option>Inventory / supplies</option><option>Cash flow</option><option>Marketing</option><option>Other business purpose</option></select>
<label for="msg">Message</label><textarea id="msg" rows="4" placeholder="Tell us about your business and how you'd use the funds. Please don't include SSNs or bank details."></textarea>
<label style="font-weight:400;display:flex;gap:10px;align-items:flex-start"><input type="checkbox" id="bp" required style="width:auto;margin-top:6px"> I confirm this request is for a business purpose, not personal, family, or household use. *</label>
<p style="margin-top:18px"><button class="btn" type="submit">Send inquiry by email</button></p><p class="note">Submitting an inquiry is not a loan application approval or commitment to lend. See our <a href="privacy.html">Privacy Policy</a>.</p></form>
<script>f.addEventListener('submit',e=>{{e.preventDefault();const v=id=>document.getElementById(id).value.trim();
const body=`Name: ${{v('name')}}\\nBusiness: ${{v('biz')}}\\nEmail: ${{v('em')}}\\nPhone: ${{v('ph')}}\\nAmount requested: ${{v('amt')}}\\nPurpose: ${{v('pur')}}\\nBusiness-purpose confirmed: Yes\\n\\nMessage:\\n${{v('msg')}}`;
location.href='mailto:{EMAIL}?subject='+encodeURIComponent('Business loan inquiry - '+v('biz'))+'&body='+encodeURIComponent(body)}});</script>
<p class="note">{DISC}</p></div></section>''')
T='<div class="notice"><b>TEMPLATE: for attorney review.</b> This is a draft placeholder, not final legal language. It must be reviewed and completed by a qualified Texas attorney before being relied on.</div>'
P['privacy.html']=('Privacy Policy','Privacy Policy (template) for Apex Elite Lending LLC.',f'''<div class="page-h"><div class="wrap"><h1>Privacy Policy</h1><p>Last updated: [DATE], TEMPLATE</p></div></div><section class="legal"><div class="wrap" style="max-width:820px">{T}
<p>Apex Elite Lending LLC ("we," "us") respects your privacy. This policy describes how we handle information collected through this website and in connection with business-purpose loan inquiries. <b>{DISC}</b></p>
<h2>Information we collect</h2><p>This website does not use forms that store data on our servers. When you use the inquiry form, your device opens an email you choose to send us, containing the name, business name, email, phone, amount, purpose, and message you entered. Our hosting provider may automatically log technical data such as IP address and browser type. [Attorney: confirm hosting/analytics disclosures.]</p>
<h2>How we use information</h2><p>To respond to inquiries, evaluate business-purpose loan requests, service loans, comply with law, and prevent fraud.</p>
<h2>Sharing</h2><p>We do not sell personal information. We may share information with service providers, credit bureaus (with your consent), and as required by law. [Attorney: complete, including any GLBA requirements if applicable.]</p>
<h2>Security</h2><p>We use reasonable safeguards. Please do not send sensitive information such as Social Security or bank account numbers by email or website form.</p>
<h2>Your choices & contact</h2><p>Questions or requests: <a href="mailto:{EMAIL}">{EMAIL}</a> {TODO}.</p><h2>Changes</h2><p>We may update this policy and will post the revised date above.</p></div></section>''')
P['terms.html']=('Terms of Use','Terms of Use (template) for the Apex Elite Lending LLC website.',f'''<div class="page-h"><div class="wrap"><h1>Terms of Use</h1><p>Last updated: [DATE], TEMPLATE</p></div></div><section class="legal"><div class="wrap" style="max-width:820px">{T}
<h2>About this site</h2><p>This website is operated by Apex Elite Lending LLC, Frisco, Texas. <b>{DISC}</b> Personal loans are coming soon, pending Texas licensing, and are not currently offered.</p>
<h2>No offer or commitment</h2><p>Information on this site, including rates, amounts, and calculator results, is for illustration only and is not an offer, quote, or commitment to lend. All loans are subject to application, underwriting, approval, and a signed written agreement. Approval is not guaranteed.</p>
<h2>Business purpose</h2><p>Loans are made only for business, commercial, or similar purposes and not for personal, family, or household purposes.</p>
<h2>Acceptable use</h2><p>Don't misuse the site, submit false information, or attempt to disrupt it.</p><h2>Disclaimers & limitation of liability</h2><p>The site is provided "as is." [Attorney: complete.]</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of Texas. [Attorney: confirm venue.]</p><h2>Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a> {TODO}</p></div></section>''')
for fn,(t,d,b) in P.items(): open(fn,'w').write(page(fn,t,d,b))
print(list(P))
