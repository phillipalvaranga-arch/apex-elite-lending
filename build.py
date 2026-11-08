EMAIL='contact@apexelitelending.com'
TODO=''
def todo(prefix=' '):
    return f'{prefix}{TODO}' if TODO else ''
# Bump when published content changes so installed copies drop the previous cache.
ASSET_VERSION='1'
CACHE_NAME=f'apex-elite-v{ASSET_VERSION}'
DISC='Business-purpose loans only. Not a consumer lender at this time.'
NAV=[('index.html','Home'),('business-loans.html','Business Loans'),('personal-loans-jamaica.html','Personal Loans (Jamaica)'),('about.html','About'),('faq.html','FAQ'),('contact.html','Contact')]
def link(h,t,fn=None):
    on=' class=on' if fn and h==fn else ''
    gold=' style="color:var(--gold)"' if h=='personal-loans-jamaica.html' else ''
    return f'<a href="{h}"{on}{gold}>{t}</a>'
def page(fn,title,desc,body):
    links=''.join(link(h,t,fn) for h,t in NAV)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Apex Elite Lending LLC</title><meta name="description" content="{desc}"><meta name="theme-color" content="#0a1628">
<meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Apex Elite"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="icon" href="favicon.png"><link rel="apple-touch-icon" href="apple-touch-icon.png"><link rel="manifest" href="manifest.json"><link rel="stylesheet" href="style.css?v={ASSET_VERSION}"></head><body>
<header><div class="wrap nav"><a class="brand" href="index.html"><img src="logo.png" alt="Apex Elite logo" width="40" height="40">Apex Elite <span>Lending</span></a>
<button id="mt" aria-label="Menu" onclick="document.querySelector('nav.links').classList.toggle('open')">☰</button>
<nav class="links">{links}<a class="btn" href="apply.html">Apply</a></nav></div></header>
<main>{body}</main>
<footer><div class="wrap"><div class="fgrid"><div><a class="brand" href="index.html" style="display:flex"><img src="logo.png" alt="" width="32" height="32">Apex Elite <span>Lending</span> LLC</a>
<p>Small business-purpose loans for Texas entrepreneurs. Based in Frisco, Texas.</p><p>Email: <a style="display:inline" href="mailto:{EMAIL}">{EMAIL}</a>{todo()}</p></div>
<div><b>Company</b>{''.join(link(h,t) for h,t in NAV)}</div><div><b>Get started</b><a href="apply.html">Apply</a><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a></div></div>
<div class="disc"><b>{DISC}</b> Personal loans in Jamaica are <a style="display:inline" href="personal-loans-jamaica.html">coming soon, launching once licensed by the Bank of Jamaica</a>; Apex Elite Lending LLC does not currently offer, make, or arrange consumer loans in Texas or Jamaica. All loans are subject to application, review, and approval. Rates shown are maximums and examples, not offers. © 2026 Apex Elite Lending LLC, Frisco, Texas.</div></div></footer>
<script>if('serviceWorker' in navigator){{navigator.serviceWorker.register('sw.js').catch(function(){{}})}}</script>
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
<div class="card"><span class="pill">Coming soon</span><h3>Personal loans: Jamaica</h3><p>We're preparing personal loans for people living in Jamaica, launching once licensed by the Bank of Jamaica. <a href="personal-loans-jamaica.html">See the plan and calculator</a>.</p></div>
<div class="card"><h3>Fair & consistent</h3><p>Every application is reviewed against the same written criteria. We never promise "guaranteed approval."</p></div></div>
<div class="notice">{DISC} Personal loans for borrowers in Jamaica are <a href="personal-loans-jamaica.html">coming soon, launching once licensed by the Bank of Jamaica</a>.</div></div></section>''')
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
<div class="notice"><b>Want to know when personal loans are available?</b><br>Email <a href="mailto:{EMAIL}?subject=Personal%20loans%20-%20notify%20me&body=Please%20let%20me%20know%20when%20personal%20loans%20become%20available.">{EMAIL}</a>{todo()} with the subject "Notify me." Joining the interest list is not an application and is not a commitment to lend.</div>
<div class="notice"><b>New: Personal loans for Jamaica.</b> We're preparing personal loans for borrowers living in Jamaica, launching once licensed by the Bank of Jamaica. <a href="personal-loans-jamaica.html">See Personal Loans: Jamaica</a>.</div>
<p>If you need funding for a <b>business purpose</b>, see our <a href="business-loans.html">business loans</a>.</p><p class="note">{DISC}</p></div></section>''')
PLANNED_USES=['Earnest money','Home inspection','Home appraisal','Loan origination fee','Title insurance','Escrow and settlement fees','Property survey','Homeowners insurance','Prepaid property taxes','Moving expenses']
JMFAQ=[('Can I apply today?','Not yet. Apex Elite Lending is not yet licensed by the Bank of Jamaica, and in Jamaica it is an offence to offer microcredit without a licence. You can join the interest list, and we will contact you when we launch.'),
('Is joining the interest list an application?','No. It only tells us you are interested. It is not an application, an approval, or a promise to lend.'),
('What interest rate will I pay?','We have not set rates yet. Jamaican law requires a licensed lender to tell you the rate and how it is calculated in writing, and to show the Effective Annual Interest Rate (EAIR) most prominently. You will see all of this before you sign anything.'),
('Can interest be charged on the original amount the whole time?','No. Under the Microcredit Act, interest and late penalties must be calculated on the outstanding balance, not the original amount borrowed.'),
('Why does the form not ask for my TRN?',"To protect you. We will never ask for your TRN, bank details, or card numbers through this website. After we are licensed, identity checks will be done through a secure process."),
('Will I be paid in Jamaican dollars?','We expect loans to be made and repaid in Jamaican dollars (JMD). The USD view in the calculator is only for comparison.'),
('How can I check whether a lender is licensed?','The Bank of Jamaica publishes its list of licensed microcredit institutions on its website. Always check it before borrowing from anyone, including us.'),
('Where can I complain about a lender in Jamaica?','The Consumer Affairs Commission (CAC) handles consumer complaints about licensed microcredit institutions.'),
('Which home-buying and moving costs are planned?','None are available today. After licensing, we plan to consider personal loans for '+', '.join(PLANNED_USES[:-1])+', and '+PLANNED_USES[-1]+'. These are planned uses, not approved products, and approval is not guaranteed. If borrowed funds are used in a home purchase, the mortgage lender\'s approval and disclosure requirements may apply. Amounts, rates, and terms are not set.')]
P['personal-loans-jamaica.html']=('Personal Loans: Jamaica (Coming Soon)','Personal loans for borrowers in Jamaica from Apex Elite Lending, coming soon and launching once licensed by the Bank of Jamaica.',f'''
<div class="page-h"><div class="wrap"><span class="pill">Coming soon</span><h1 style="color:var(--gold)">Personal Loans: Jamaica</h1><p>Launching once licensed by the Bank of Jamaica.</p></div></div>
<section><div class="wrap" style="max-width:860px"><div class="notice"><b>We are not lending in Jamaica yet.</b> Apex Elite Lending LLC is <b>not currently licensed</b> by the Bank of Jamaica under the Microcredit Act, 2021, and does not offer, make, or arrange personal loans in Jamaica today. We are not taking applications. This page explains our plans so you know what to expect.</div>
<p>We plan to offer small, fixed-payment personal loans to people living in Jamaica, in Jamaican dollars, with every cost shown in writing before you sign. You can always check whether any lender is licensed on the <a href="https://boj.org.jm/core-functions/financial-system/microcredit-regulation/list-of-licensed-microcredit-institutions/" target="_blank" rel="noopener">Bank of Jamaica's list of licensed microcredit institutions</a>.</p></div></section>
<section id="planned-uses"><div class="wrap" style="max-width:860px"><h2>Planned personal loan uses</h2>
<p class="lead">Once personal loans launch in Jamaica, we plan to consider them for home-buying and closing costs, and for moving expenses. These are planned uses only. They are not available today, not approved products, and not a promise that a loan will be approved.</p>
<ul class="check uses">{''.join(f'<li>{u}</li>' for u in PLANNED_USES)}</ul>
<p class="note">If borrowed funds are used in a home purchase, the mortgage lender's approval and disclosure requirements may apply. Amounts, rates, and terms for these uses are not set.</p></div></section>
<section class="alt" id="calculator"><div class="wrap"><h2>Personal loan calculator</h2><p class="lead">See what a loan could cost. This is an illustration only, not an offer, a quote, or our rate.</p>
<div class="card" style="max-width:720px"><div class="row2"><div><label for="cur">Currency</label><select id="cur"><option value="JMD" selected>Jamaican dollars (JMD)</option><option value="USD">US dollars (USD)</option></select></div>
<div><label for="fx">Exchange rate (JMD per US$1)</label><input id="fx" type="number" min="1" step="0.5" value="160"></div>
<div><label for="jamt">Loan amount (<span id="cl">JMD</span>)</label><input id="jamt" type="number" min="0" step="1000" value="200000"></div>
<div><label for="jrate">Annual interest rate (%)</label><input id="jrate" type="number" min="0" max="200" step="0.5" value="30"></div>
<div><label for="jterm">Term (months)</label><input id="jterm" type="number" min="1" max="60" step="1" value="12"></div></div>
<div class="grid" style="margin-top:18px"><div><p class="note">Monthly payment</p><p class="out" id="jpay">-</p></div><div><p class="note">Total interest</p><p class="out" id="jint">-</p></div><div><p class="note">Total repaid</p><p class="out" id="jtot">-</p></div><div><p class="note">Effective annual rate (EAIR)</p><p class="out" id="jeair">-</p></div></div>
<h3 style="margin-top:22px">Payment summary</h3><div class="schedule"><table id="am" style="width:100%;border-collapse:collapse;font-size:15px"></table></div>
<p class="note">Assumes equal monthly payments, interest charged monthly on the remaining balance, and no fees. EAIR = (1 + rate ÷ 12)<sup>12</sup> − 1. The exchange rate is a rough example you can change; check a current rate with your bank or the Bank of Jamaica. Real loans may include fees and different terms, all shown in writing before you sign.</p></div>
<script>
const f0=(v,c)=>(c=='JMD'?'J$':'US$')+v.toLocaleString(undefined,{{minimumFractionDigits:2,maximumFractionDigits:2}});
let lastCur='JMD';
cur.addEventListener('change',()=>{{let x=+fx.value||1,a=+jamt.value||0;jamt.value=cur.value=='USD'&&lastCur=='JMD'?(a/x).toFixed(0):cur.value=='JMD'&&lastCur=='USD'?(a*x).toFixed(0):a;lastCur=cur.value;cl.textContent=cur.value;jc()}});
function jc(){{const c=cur.value,a=Math.max(0,+jamt.value||0),R=Math.max(0,+jrate.value||0),r=R/1200,n=Math.max(1,Math.round(+jterm.value||1));
const p=r?a*r/(1-Math.pow(1+r,-n)):a/n;jpay.textContent=f0(p,c);jint.textContent=f0(p*n-a,c);jtot.textContent=f0(p*n,c);jeair.textContent=((Math.pow(1+r,12)-1)*100).toFixed(2)+'%';
let b=a,rows=[],yi=0,yp=0,yr=1;for(let m=1;m<=n;m++){{const i=b*r,pr=p-i;b=Math.max(0,b-pr);yi+=i;yp+=pr;if(m%12==0||m==n){{rows.push(`<tr><td>Year ${{yr}} (to month ${{m}})</td><td>${{f0(yp,c)}}</td><td>${{f0(yi,c)}}</td><td>${{f0(b,c)}}</td></tr>`);yr++;yi=0;yp=0}}}}
am.innerHTML='<tr style="text-align:left;color:var(--gold)"><th>Period</th><th>Principal paid</th><th>Interest paid</th><th>Balance left</th></tr>'+rows.join('');
am.querySelectorAll('td,th').forEach(e=>{{e.style.padding='8px';e.style.borderBottom='1px solid var(--line)'}})}}
['fx','jamt','jrate','jterm'].forEach(i=>document.getElementById(i).addEventListener('input',jc));jc();</script></div></section>
<section><div class="wrap"><div class="grid">
<div class="card"><h3>Who can apply (once we launch)</h3><ul class="check"><li>Adults 18 or older living in Jamaica</li><li>A valid Jamaican government photo ID</li><li>Steady income you can show</li><li>A clear ability to repay, which we must check</li></ul><p class="note">Final rules will be set when we are licensed. Approval will never be guaranteed.</p></div>
<div class="card"><h3>Documents usually needed</h3><ul class="check"><li><b>Jamaican ID:</b> driver's licence, passport, or national voter ID</li><li><b>TRN (Taxpayer Registration Number):</b> required for identity checks, but collected only through our secure process later, <b>never on this website</b></li><li><b>Proof of income:</b> recent pay slips, a job letter, or bank statements</li><li><b>Proof of address:</b> a recent utility bill or bank statement</li></ul></div></div>
<h2 style="margin-top:50px">How it will work</h2><div class="grid">
<div class="card"><div class="num">1</div><h3>Join the interest list</h3><p>Name, contact, and a rough amount. Nothing sensitive.</p></div>
<div class="card"><div class="num">2</div><h3>We contact you after licensing</h3><p>Once the Bank of Jamaica licenses us, we reach out and explain the next steps.</p></div>
<div class="card"><div class="num">3</div><h3>Secure review</h3><p>We verify your identity and check that the loan is affordable for you, as the law requires.</p></div>
<div class="card"><div class="num">4</div><h3>Written terms, then funding</h3><p>You get the full agreement, with rate, EAIR, fees, and payment dates, before you sign. Then funds are sent and you repay in fixed monthly payments.</p></div></div></div></section>
<section class="alt" id="interest"><div class="wrap" style="max-width:760px"><h2>Join the interest list</h2><p class="lead">This is not an application. We will only contact you once we are licensed.</p>
<div class="notice"><b>Do not include sensitive information.</b> Never send your TRN, bank or card numbers, or passwords. When you press Send, your own email app opens with a prefilled message to {EMAIL}{todo()}. Nothing is stored on this website.</div>
<form class="card" id="jf"><div class="row2"><div><label for="jn">Full name *</label><input id="jn" required autocomplete="name"></div><div><label for="je">Email or phone *</label><input id="je" required autocomplete="email"></div></div>
<label for="ja">Rough amount you might need *</label><select id="ja" required><option value="">Select…</option><option>Under J$100,000</option><option>J$100,000 to J$250,000</option><option>J$250,000 to J$500,000</option><option>Over J$500,000</option></select>
<p style="margin-top:18px"><button class="btn" type="submit">Send by email</button></p><p class="note">Joining is not an application and is not a commitment to lend. See our <a href="privacy.html">Privacy Policy</a>.</p></form>
<script>jf.addEventListener('submit',e=>{{e.preventDefault();const v=i=>document.getElementById(i).value.trim();
location.href='mailto:{EMAIL}?subject='+encodeURIComponent('Jamaica personal loans - interest list')+'&body='+encodeURIComponent(`Name: ${{v('jn')}}\\nEmail or phone: ${{v('je')}}\\nRough amount: ${{v('ja')}}\\n\\nPlease contact me when personal loans in Jamaica are available.`)}});</script></div></section>
<section><div class="wrap" style="max-width:820px"><h2>Questions</h2>{''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in JMFAQ)}
<h2 style="margin-top:40px">Important disclosures</h2><div class="notice">
<p><b>Not licensed yet.</b> Apex Elite Lending LLC (Frisco, Texas, USA) is not currently licensed by the Bank of Jamaica as a microcredit institution and does not currently offer, make, or arrange loans in Jamaica. No applications are being accepted.</p>
<p><b>No offer or guarantee.</b> Calculator results are examples only, not offers, quotes, or our rates. Any future loan will depend on application, identity checks, an affordability review, approval, and a signed written agreement. Approval is never guaranteed.</p>
<p><b>Rates.</b> When we lend, we will state the interest rate and how it is calculated in writing, show the Effective Annual Interest Rate (EAIR) most prominently, and charge interest and late penalties only on the outstanding balance, as required by the <a href="https://japarliament.gov.jm/attachments/article/339/The%20Microcredit%20Act,%202021.pdf" target="_blank" rel="noopener">Microcredit Act, 2021</a>.</p>
<p><b>Identity checks.</b> Licensed lenders in Jamaica must verify customer identity and follow anti-money-laundering laws, including the Proceeds of Crime Act.</p>
<p><b>Complaints.</b> Consumer complaints about licensed microcredit lenders can be made to the Consumer Affairs Commission of Jamaica.</p>
<p><b>Planned uses.</b> The home-buying, closing, and moving costs on this page are planned uses only. They are not offers and not approved products. If borrowed funds are used in a home purchase, the mortgage lender's approval and disclosure requirements may apply.</p></div>
<p>Need a loan for a Texas business? See our <a href="business-loans.html">business loans</a>.</p></div></section>''')

P['about.html']=('About Us','About Apex Elite Lending LLC, a small business lender based in Frisco, Texas.',f'''
<div class="page-h"><div class="wrap"><h1>About Apex Elite Lending</h1><p>A Frisco, Texas company focused on small business funding.</p></div></div>
<section><div class="wrap" style="max-width:820px"><p>Apex Elite Lending LLC is a new, independently owned lending company based in Frisco, Texas. We started with a simple idea: small businesses sometimes need a small amount of capital, and they deserve a lender who treats a $1,500 request as seriously as a large one.</p>
<p>We're starting deliberately small, making business-purpose loans of $1,000 to $2,500 at no more than 18% APR, so we can serve each borrower personally and build a track record the right way.</p>
<h2 style="margin-top:36px">Our commitments</h2><ul class="check"><li><b>Transparency:</b> every cost and payment in writing before you sign.</li><li><b>Fairness:</b> the same written criteria for every applicant, in line with fair-lending laws.</li><li><b>Respect:</b> professional, lawful communication at every stage, including collections.</li><li><b>Privacy:</b> we collect only what we need and protect it carefully.</li><li><b>Honesty:</b> no "guaranteed approval," no hidden fees, no pressure.</li></ul>
<h2 style="margin-top:36px">What's next</h2><p>As the company grows, we intend to apply for Texas licensing to offer personal installment loans. Until then, <b>we offer business-purpose loans only.</b></p><p><a class="btn" href="contact.html">Get in touch</a></p></div></section>''')
faq=[('Who can apply?','Texas small businesses and business owners who need funds for a business purpose, such as equipment, inventory, or cash flow.'),
('How much can I borrow?','Business-purpose loans currently range from $1,000 to $2,500. First-time borrowers may be offered a smaller amount.'),
('What is the interest rate?','Rates are fixed and never exceed 18% APR. Your rate depends on our review and appears in your written agreement before you sign.'),
('Do you offer personal loans?','Not yet. Personal loans for borrowers in Jamaica are coming soon, launching once licensed by the Bank of Jamaica. Personal loans in Texas still need Texas licensing. Today we make business-purpose loans only and are not a consumer lender. See <a href="personal-loans-jamaica.html">Personal Loans: Jamaica</a>.'),
('Can I use a business loan for personal expenses?',"No. Loans must be used primarily for business purposes, and you'll sign a business-purpose certification."),
('Do you check credit?','We may review credit as part of underwriting, only with your signed consent. A credit history alone doesn\'t decide an application.'),
('Is approval guaranteed?','No. Every application is reviewed against the same written criteria, and approval is never guaranteed.'),
('Why doesn\'t the online form ask for my SSN or bank details?',"To protect you. The website form only starts the conversation. If we move forward, we'll collect any sensitive documents through a secure method, never by regular email or website form."),
('How do I repay?','Through fixed monthly payments on a set schedule. Automatic payments may be available with your written authorization, which you can revoke.'),
('Are there prepayment penalties?','Prepayment terms will be stated in your loan agreement. Ask us before you apply.')]
P['faq.html']=('FAQ','Frequently asked questions about Apex Elite Lending business loans.','<div class="page-h"><div class="wrap"><h1>Frequently Asked Questions</h1></div></div><section><div class="wrap" style="max-width:820px">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)+'<p style="margin-top:30px">Still have a question? <a href="contact.html">Contact us</a>.</p></div></section>')
P['contact.html']=('Contact','Contact Apex Elite Lending LLC in Frisco, Texas.',f'''
<div class="page-h"><div class="wrap"><h1>Contact Us</h1><p>We'd love to hear about your business.</p></div></div>
<section><div class="wrap"><div class="grid"><div class="card"><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a>{todo('<br>')}</p></div>
<div class="card"><h3>Phone</h3><p><span class="todo">TODO: add business phone</span></p></div>
<div class="card"><h3>Location</h3><p>Frisco, Texas<br><span class="todo">TODO: add mailing address if desired</span></p></div></div>
<div class="notice">Please don't email Social Security numbers, bank account numbers, or other sensitive information. We'll arrange a secure way to collect documents if needed.</div>
<p><a class="btn" href="apply.html">Start an application</a></p></div></section>''')
P['apply.html']=('Apply','Start a business-purpose loan inquiry with Apex Elite Lending.',f'''
<div class="page-h"><div class="wrap"><h1>Apply for a Business Loan</h1><p>Start with a quick inquiry. We'll follow up personally.</p></div></div>
<section><div class="wrap" style="max-width:760px"><div class="notice"><b>Do not include sensitive information.</b> This form never asks for your Social Security number, bank account details, or ID numbers. When you press Send, it opens a prefilled email in your own mail app addressed to {EMAIL}{todo()}. Nothing is stored on this website.</div>
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
<h2>Your choices & contact</h2><p>Questions or requests: <a href="mailto:{EMAIL}">{EMAIL}</a>{todo()}.</p><h2>Changes</h2><p>We may update this policy and will post the revised date above.</p></div></section>''')
P['terms.html']=('Terms of Use','Terms of Use (template) for the Apex Elite Lending LLC website.',f'''<div class="page-h"><div class="wrap"><h1>Terms of Use</h1><p>Last updated: [DATE], TEMPLATE</p></div></div><section class="legal"><div class="wrap" style="max-width:820px">{T}
<h2>About this site</h2><p>This website is operated by Apex Elite Lending LLC, Frisco, Texas. <b>{DISC}</b> Personal loans are coming soon, pending Texas licensing, and are not currently offered.</p>
<h2>No offer or commitment</h2><p>Information on this site, including rates, amounts, and calculator results, is for illustration only and is not an offer, quote, or commitment to lend. All loans are subject to application, underwriting, approval, and a signed written agreement. Approval is not guaranteed.</p>
<h2>Business purpose</h2><p>Loans are made only for business, commercial, or similar purposes and not for personal, family, or household purposes.</p>
<h2>Acceptable use</h2><p>Don't misuse the site, submit false information, or attempt to disrupt it.</p><h2>Disclaimers & limitation of liability</h2><p>The site is provided "as is." [Attorney: complete.]</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of Texas. [Attorney: confirm venue.]</p><h2>Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a>{todo()}</p></div></section>''')
for fn,(t,d,b) in P.items(): open(fn,'w').write(page(fn,t,d,b))
from string import Template
assets=[f'./{fn}' for fn in P]+[f'./style.css?v={ASSET_VERSION}','./style.css','./manifest.json','./favicon.png','./apple-touch-icon.png','./logo.png']
open('sw.js','w').write(Template(r'''/* Generated by build.py. Bump ASSET_VERSION there when publishing content changes. */
const CACHE='$cache';
const ASSETS=[$assets];
self.addEventListener('install',event=>{event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(ASSETS)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>key!==CACHE).map(key=>caches.delete(key)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',event=>{const req=event.request;if(req.method!=='GET')return;event.respondWith((async()=>{const url=new URL(req.url);if(url.origin!==self.location.origin)return fetch(req);try{const fresh=await fetch(req);if(fresh&&fresh.ok){const cache=await caches.open(CACHE);cache.put(req,fresh.clone())}return fresh}catch(err){const cached=await caches.match(req);if(cached)return cached;if(req.mode==='navigate'){const home=await caches.match('./index.html');if(home)return home}throw err}})())});
''').substitute(cache=CACHE_NAME,assets=','.join("'"+a+"'" for a in assets)))
open('manifest.json','w').write('''{
  "name": "Apex Elite Lending",
  "short_name": "Apex Elite",
  "description": "Apex Elite Lending LLC. Business-purpose loans in Texas. Personal loans in Jamaica are coming soon.",
  "start_url": "./index.html",
  "scope": "./",
  "display": "standalone",
  "background_color": "#0a1628",
  "theme_color": "#0a1628",
  "icons": [
    {"src": "apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
    {"src": "logo.png", "sizes": "256x256", "type": "image/png"},
    {"src": "favicon.png", "sizes": "64x64", "type": "image/png"}
  ]
}
''')
jamaica=open('personal-loans-jamaica.html').read()
missing=[u for u in PLANNED_USES if u not in jamaica]
if missing: raise SystemExit('missing planned uses: '+', '.join(missing))
for required in ['style="color:var(--gold)"','id="calculator"','Can I apply today?','not currently licensed','Coming soon','id="jn"','id="je"','id="ja"','serviceWorker.register','manifest.json','mortgage lender\'s approval and disclosure requirements may apply','not approved products']:
    if required not in jamaica: raise SystemExit('jamaica page missing: '+required)
if 'type="password"' in jamaica.lower() or 'name="ssn"' in jamaica.lower() or 'name="trn"' in jamaica.lower():
    raise SystemExit('sensitive field added')
contact=open('contact.html').read()
for required in ['TODO: add business phone','TODO: add mailing address if desired','contact@apexelitelending.com']:
    if required not in contact: raise SystemExit('contact page changed: '+required)
if 'TODO: confirm email' in contact: raise SystemExit('email placeholder returned')
sw=open('sw.js').read()
if CACHE_NAME not in sw: raise SystemExit('cache name missing')
if "req.method!=='GET'" not in sw: raise SystemExit('service worker must ignore non-GET')
print(list(P), CACHE_NAME, 'uses', len(PLANNED_USES))
