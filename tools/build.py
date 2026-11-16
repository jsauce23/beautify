import json, os

OUT = os.environ.get('DC_OUT', '/home/claude/bs/project')

# ---------- tokens ----------
PAPER = '#F7F0EC'
INK = '#1A1314'
ROSE = '#8E4B57'
WINE = '#4A1F28'
BLUSH = '#EED9D4'
LINE = '#DCC6C1'
MUTED = '#463A3C'
DISP = "font-family: 'DM Serif Display', Georgia, serif"

BOOK_URL = 'book.dc.html'
ADDR1 = '1603 Babcock Rd, Suite 230'
ADDR2 = 'San Antonio, TX 78229'
PHONE = '(726) 242-2952'
TEL = 'tel:+17262422952'
EMAIL = 'beautifiedstudios@gmail.com'
IG = 'https://www.instagram.com/beautified.studios/'
FB = 'https://www.facebook.com/profile.php?id=100071732994266'

EYEBROW = f'margin: 0 0 18px; font-size: 14px; font-weight: 500; letter-spacing: 0.14em; text-transform: uppercase; color: {ROSE}'
EYEBROW_D = 'margin: 0 0 18px; font-size: 14px; font-weight: 500; letter-spacing: 0.14em; text-transform: uppercase; color: #E7B9C1'
H2 = f'margin: 0; {DISP}; font-weight: 400; font-size: clamp(40px, 5.2vw, 76px); line-height: 1.02; letter-spacing: -0.01em'
H3 = f'margin: 0; {DISP}; font-weight: 400; font-size: 30px; line-height: 1.15; letter-spacing: -0.01em'
P = f'margin: 0; color: {MUTED}'
BTN = f'display: inline-block; background: {WINE}; color: {PAPER}; text-decoration: none; padding: 18px 34px; border-radius: 999px; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase'
BTN_O = f'display: inline-block; border: 1px solid {INK}; color: {INK}; text-decoration: none; padding: 17px 32px; border-radius: 999px; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase'
BTN_L = f'display: inline-block; background: {PAPER}; color: {WINE}; text-decoration: none; padding: 18px 34px; border-radius: 999px; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase'
WRAP = 'max-width: 1320px; margin: 0 auto; padding-left: 32px; padding-right: 32px; box-sizing: border-box'

HELMET = f'''<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&amp;family=Jost:wght@300;400;500;600&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{PAPER}}}
a{{color:{ROSE}}}a:hover{{color:{WINE}}}
html{{scroll-behavior:smooth}}
summary{{list-style:none}}summary::-webkit-details-marker{{display:none}}
input:focus,button:focus-visible,a:focus-visible,summary:focus-visible{{outline:2px solid {ROSE};outline-offset:3px}}
button:disabled{{opacity:.4;cursor:not-allowed}}
.nav-links{{display:flex}}.nav-mobile{{display:none}}
@media (max-width:900px){{.nav-links{{display:none!important}}.nav-mobile{{display:flex!important}}.tb-addr{{display:none!important}}.wm-big{{font-size:21px!important}}.wm-small{{margin-top:5px!important}}.ov-card{{position:static!important;margin:0!important;max-width:none!important;padding:32px 24px!important}}}}
</style>
</helmet>'''

PHOTOS = [
    ('P01', 'Brandy, hero portrait', 'Vertical, polished portrait of Brandy against a clean background. Looking at the camera.', 'Home hero, About page', 'Vertical'),
    ('P02', 'Brandy injecting a client', 'Brandy mid treatment with a client. Gloves on, natural light.', 'Home hero (round photo)', 'Square or vertical'),
    ('P03', 'Front facing model portrait', 'A client or model facing the camera straight on, neutral expression, even lighting. Used for the tap-to-explore face map.', 'Home face map', 'Vertical'),
    ('P04', 'Studio interior', 'Wide shot of the studio showing the treatment chair and decor.', 'Location sections, Stone Oak page', 'Horizontal'),
    ('P05', 'Treatment room detail', 'Close detail of the chair, products or decor.', 'Location sections', 'Horizontal'),
    ('P06', 'Brandy, candid portrait', 'A second, more relaxed portrait of Brandy.', 'Home About section', 'Vertical'),
    ('P07', 'Lip filler before and after', 'Same angle and lighting before and after. Client consent required.', 'Home results, Lip Filler page, Leon Valley page', 'Vertical'),
    ('P08', 'Jawline before and after', 'Front and side profile of a jaw filler client.', 'Jaw Filler page, Stone Oak page', 'Vertical'),
    ('P09', 'Nose before and after', 'Side profile before and after a non-surgical nose job.', 'Nose Job page, Helotes page', 'Vertical'),
    ('P10', 'Forehead and frown lines before and after', 'Daxxify client, lines visible before and softened after.', 'Daxxify page, Alamo Heights page', 'Square'),
    ('P11', 'Facial balancing before and after', 'Full face before and after a balancing treatment.', 'Facial Balancing page, Boerne page, Blog', 'Vertical'),
    ('P12', 'Lip flip before and after', 'Close up of the upper lip before and after a lip flip.', 'Lip Flip page, Medical Center page', 'Square'),
    ('P13', 'Daxxify and RHA products', 'Styled shot of the products she uses.', 'Daxxify blog post', 'Horizontal'),
    ('P14', 'Brandy teaching a class', 'Brandy training an injector student.', 'About page, Training section', 'Horizontal'),
    ('P16', 'Building entrance and suite sign', 'The building front and the Suite 230 sign so clients can find her.', 'Location sections on every page', 'Horizontal'),
    ('P17', 'Lips close up', 'A fresh, glossy lip result close up.', 'Lip Flip page, Blog', 'Square'),
    ('P18', 'Weekly blog photo', 'One new photo for each weekly blog post.', 'Blog', 'Horizontal'),
    ('P19', 'Chin filler result', 'Side profile showing chin filler.', 'Lip Filler page', 'Vertical'),
    ('P20', 'Cheek filler result', 'Three quarter view showing cheek filler.', 'Lip Filler page', 'Vertical'),
    ('P22', 'Teeth whitening before and after', 'Close up smile before and after whitening, same lighting.', 'Teeth Whitening page', 'Horizontal'),
    ('P23', 'Tooth gem close up', 'A smile showing a finished tooth gem.', 'Tooth Gems and Teeth Whitening pages', 'Square'),
    ('P24', 'Brow color correction before and after', 'Brows before and after color correction.', 'Brow Color Correction page', 'Vertical'),
    ('P25', 'Lip blush before and after', 'Lips before and after lip blush, same angle.', 'Lip Blush page', 'Vertical'),
    ('P26', 'Academy graduate photo', 'Brandy with a student holding a certificate.', 'Academy page', 'Vertical'),
    ('P27', 'Academy class in session', 'Brandy teaching a 1:1 student at the table.', 'Academy page', 'Horizontal'),
    ('P21', 'Second lip filler result', 'Another lip result, before, during and after works great.', 'Home results, Lip Filler page', 'Vertical'),
]
PH = {c: (t, d) for c, t, d, _, _ in PHOTOS}

def ph(code, label, style=''):
    if code == 'MAP':
        title, detail = label, 'We create this map. Nothing needed from Brandy.'
    else:
        title, detail = PH.get(code, (label, ''))
        title = label if label and code not in PH else title
    cam = '<svg aria-hidden="true" width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#8E4B57" stroke-width="1.3"><path d="M3 8h3l2-3h8l2 3h3v11H3z"></path><circle cx="12" cy="13" r="4"></circle></svg>'
    tag = 'Map' if code == 'MAP' else f'Photo needed · {code}'
    return (f'<div style="background: {BLUSH}; position: relative; overflow: hidden; border: 1px dashed #C9A9A6; box-sizing: border-box; display: flex; align-items: center; justify-content: center; text-align: center; {style}">'
            f'<div style="padding: 24px; max-width: 360px; display: flex; flex-direction: column; align-items: center; gap: 10px">{cam}'
            f'<span style="font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: {ROSE}">{tag}</span>'
            f'<span style="font-family: \'DM Serif Display\', Georgia, serif; font-size: 22px; line-height: 1.2; color: {INK}">{title}</span>'
            f'<span style="font-size: 14px; line-height: 1.5; color: #463A3C">{detail}</span></div></div>')

# ---------- data ----------
SERVICES = [
    dict(id='rha', slug='lip-filler-san-antonio', short='Lip, Chin &amp; Cheek Filler', nav='Lip Filler',
         h1='Lip Filler, Chin &amp; Cheek Filler in San Antonio, TX',
         title='Lip Filler San Antonio | RHA Lip, Chin &amp; Cheek Filler | Beautified Studios',
         meta='RHA lip filler, chin filler and cheek filler in San Antonio, TX by Master Injector Brandy Gonzalez. Natural, balanced results. Book online.',
         price='Priced at consult', dur='60 min', tag='RHA filler',
         line='Add volume and shape to your lips, chin or cheeks with RHA filler.',
         intro='Brandy uses RHA filler, a hyaluronic acid filler designed to move naturally with your expressions. Whether you want a soft boost in your lips, more definition at the chin or volume in the cheeks, your plan is built around your proportions.',
         what='Hyaluronic acid filler placed to add volume, shape and smoothness where you want it most.',
         who='Clients who want more volume or shape in the lips, chin or cheeks with a natural finish.',
         expect='A consultation on your goals, numbing for comfort, then precise placement. Most visits take about an hour.',
         faqs=[('How much is lip filler at Beautified Studios?', 'Filler pricing depends on how much product your goals call for, so Brandy confirms it at your consultation. Pay later financing is available in studio for treatments from $50 to $4,000.'),
               ('Why RHA filler?', 'RHA fillers are made to flex with your face when you talk and smile, which helps results look natural in motion, not just in photos.'),
               ('Can I do lips, chin and cheeks in one visit?', 'Yes. Treating more than one area together is the idea behind Full Facial Balancing, which includes three syringes and a complimentary lip flip.')],
         ba=['P07', 'Lips before / after']),
    dict(id='flip', slug='lip-flip-san-antonio', short='Lip Flip', nav='Lip Flip',
         h1='Lip Flip in San Antonio, TX',
         title='Lip Flip San Antonio | $150 | Beautified Studios',
         meta='Get a lip flip in San Antonio for $150. A subtle, natural looking pout with no filler, by Master Injector Brandy Gonzalez. Book online.',
         price='$150', dur='60 min', tag='No filler',
         line='A subtle lip lift with no filler, for $150.',
         intro='A lip flip relaxes the muscle above your upper lip so it gently rolls outward, showing a little more of your lip. It is subtle, quick and one of the easiest ways to try injectables for the first time.',
         what='A small amount of wrinkle relaxer placed along the upper lip to let it turn slightly outward.',
         who='First timers and anyone who wants a subtle change, or who shows a lot of gum when smiling.',
         expect='A short consultation and a few tiny injections. Results settle in over the following days.',
         faqs=[('How much is a lip flip?', 'A lip flip at Beautified Studios is $150.'),
               ('Lip flip or lip filler?', 'A lip flip changes how your lip sits without adding volume. Filler adds actual volume and shape. Brandy will help you choose, and some clients do both.'),
               ('Is a lip flip included in anything else?', 'Yes. Full Facial Balancing includes a complimentary lip flip.')],
         ba=['P12', 'Lip flip before / after']),
    dict(id='dax', slug='daxxify-san-antonio', short='Daxxify', nav='Daxxify',
         h1='Daxxify in San Antonio, TX',
         title='Daxxify San Antonio | Longer Lasting Wrinkle Relaxer | Beautified Studios',
         meta='Daxxify in San Antonio, TX by Brandy Gonzalez, a Daxxify expert and Master Injector. Soften frown lines with a longer lasting wrinkle relaxer.',
         price='Priced at consult', dur='60 min', tag='Wrinkle relaxer',
         line='Smooth forehead and frown lines with a longer lasting wrinkle relaxer.',
         intro='Daxxify is a wrinkle relaxing injectable, in the same family as Botox, known for lasting longer between appointments for many clients. Brandy is a Daxxify specialist and will map your treatment around how your face moves.',
         what='A neuromodulator that relaxes the muscles behind expression lines, such as frown lines between the brows.',
         who='Clients who want smoother expression lines and like the idea of spacing out their appointments.',
         expect='A consultation, a few quick injections and a gradual softening of lines over the next couple of weeks.',
         faqs=[('Is Daxxify the same as Botox?', 'They work in a similar way, relaxing the muscles that cause expression lines. Daxxify is a different formula that many clients choose because it tends to last longer.'),
               ('How much is Daxxify?', 'Pricing depends on how many areas and how much product you need, so it is confirmed at your consultation.'),
               ('Can I come back to adjust?', 'Yes. A Perfecting Session lets Brandy fine tune your results.')],
         ba=['P10', 'Forehead / frown lines before / after']),
    dict(id='jaw', slug='jaw-filler-san-antonio', short='Jaw Filler', nav='Jaw Filler',
         h1='Jaw Filler in San Antonio, TX',
         title='Jaw Filler San Antonio | Jawline Contouring | Beautified Studios',
         meta='Jaw filler and jawline contouring in San Antonio, TX for $1,449. Sculpted, defined results from Master Injector Brandy Gonzalez. Book online.',
         price='$1,449', dur='90 min', tag='Contouring',
         line='Define your jawline and sharpen your side profile with filler.',
         intro='Jaw filler adds structure along the jawline to define your profile and balance your features. Brandy plans the shape around your face so the result looks strong and refined, never overdone.',
         what='Filler placed along the jawline and angle of the jaw to create definition and contour.',
         who='Clients who want a more defined jaw, a cleaner side profile or better balance with the chin.',
         expect='A detailed consultation, numbing, then careful sculpting. Plan for about 90 minutes.',
         faqs=[('How much is jaw filler?', 'Jaw filler at Beautified Studios is $1,449. Pay later financing is available in studio.'),
               ('Can jaw filler be combined with chin filler?', 'Yes. Jaw and chin are often treated together. Full Facial Balancing is a good fit if you want several areas done.'),
               ('How long is the appointment?', 'Plan for about 90 minutes, including your consultation.')],
         ba=['P08', 'Jawline before / after']),
    dict(id='nose', slug='non-surgical-nose-job-san-antonio', short='Non-Surgical Nose Job', nav='Nose Job',
         h1='Non-Surgical Nose Job in San Antonio, TX',
         title='Non-Surgical Nose Job San Antonio | Liquid Rhinoplasty | Beautified Studios',
         meta='Non-surgical nose job (liquid rhinoplasty) in San Antonio from $1,500. Smooth bumps and refine your profile with filler. No surgery.',
         price='From $1,500', dur='90 min', tag='Liquid rhinoplasty',
         line='Smooth a bump and straighten your nose with filler. No surgery.',
         intro='Also called a liquid rhinoplasty, a non-surgical nose job uses filler to smooth bumps, straighten the look of the bridge and refine your profile. It is a precise treatment, and precision is what Brandy is known for.',
         what='Filler placed strategically on the nose to even out its shape and profile. It does not make the nose smaller.',
         who='Clients bothered by a bump, dip or uneven bridge who want a change without surgery.',
         expect='A thorough consultation, numbing and careful placement. Plan for about 90 minutes.',
         faqs=[('Is a non-surgical nose job permanent?', 'No. It uses filler, so results are temporary and there is no surgery or operating room recovery.'),
               ('How much is a non-surgical nose job?', 'It starts at $1,500, with the final price confirmed at your consultation.'),
               ('Can it make my nose smaller?', 'Filler adds volume, so it cannot reduce size. It can make the nose look straighter and more balanced.')],
         ba=['P09', 'Nose profile before / after']),
    dict(id='bal', slug='facial-balancing-san-antonio', short='Full Facial Balancing', nav='Facial Balancing',
         h1='Full Facial Balancing in San Antonio, TX',
         title='Facial Balancing San Antonio | 3 Syringes + Lip Flip | Beautified Studios',
         meta='Full facial balancing in San Antonio for $1,954. Includes 3 syringes of filler and a complimentary lip flip. Master Injector Brandy Gonzalez.',
         price='$1,954', dur='90 min', tag='Signature treatment',
         line='Three syringes of filler plus a free lip flip to balance your whole face.',
         intro='Full Facial Balancing is Brandy’s signature treatment. Instead of treating one feature in isolation, she looks at your whole face and uses filler to bring your lips, chin, jaw and cheeks into proportion. It includes three syringes and a complimentary lip flip.',
         what='A complete filler plan using three syringes across the areas that matter most for your face, plus a lip flip.',
         who='Clients who want an overall refresh, or who are unsure which single area to start with.',
         expect='An in-depth consultation and facial assessment, then treatment across several areas in one visit of about 90 minutes.',
         faqs=[('What is included in Full Facial Balancing?', 'Three syringes of filler placed where your face needs them most, plus a complimentary lip flip, for $1,954.'),
               ('Which areas are treated?', 'It depends on your face. Common areas are lips, chin, jawline and cheeks. Brandy will walk you through the plan before starting.'),
               ('Can I pay over time?', 'Yes. Pay later financing is available in studio for treatments from $50 to $4,000.')],
         ba=['P11', 'Facial balancing before / after']),
]


for _s in SERVICES: _s.setdefault('cat', 'Injectables')
SERVICES += [
    dict(id='teeth', variant='nose', cat='Smile, brows &amp; lips', slug='teeth-whitening-san-antonio', short='Teeth Whitening', nav='Teeth Whitening',
         h1='Teeth Whitening in San Antonio, TX',
         title='Teeth Whitening San Antonio | In-Studio LED Whitening | Beautified Studios',
         meta='In-studio teeth whitening in San Antonio at Beautified Studios. A brighter smile in one visit. Add a tooth gem. Book online.',
         price='[Price]', dur='[Time]', tag='In-studio whitening',
         line='A visibly brighter smile in one relaxing studio visit.',
         intro='Beautified Studios offers in-studio teeth whitening using a professional LED whitening light. You relax in the chair while the whitening gel and light work together to lift surface stains, and you leave with a brighter smile the same day.',
         what='A whitening gel is applied to the teeth and activated with a professional LED light to brighten your smile.',
         who='Anyone with surface stains from coffee, tea, wine or everyday life who wants a brighter smile before an event or just because.',
         expect='Lips and gums are protected, the gel is applied, and you relax under the light. Pair it with a tooth gem for extra sparkle.',
         faqs=[('How much is teeth whitening?', '[Confirm price with Brandy.]'),
               ('Can I add a tooth gem?', 'Yes. Many clients finish their whitening with a tooth gem in the same visit.'),
               ('Is teeth whitening the same as dental bleaching at a dentist?', 'In-studio cosmetic whitening is a non-dental beauty service focused on brightening surface stains. For dental concerns, see your dentist.')],
         ba=['P22', 'Teeth whitening before and after'], ba_labels=('Before', 'After')),
    dict(id='gem', variant='flip', cat='Smile, brows &amp; lips', slug='tooth-gems-san-antonio', short='Tooth Gems', nav='Tooth Gem',
         h1='Tooth Gems in San Antonio, TX',
         title='Tooth Gems San Antonio | Beautified Studios',
         meta='Tooth gems in San Antonio at Beautified Studios. A little sparkle bonded to your smile, no drilling. Pair with teeth whitening. Book online.',
         price='[Price]', dur='[Time]', tag='No drilling', big='✦', compare=('#how', 'How it works'), extra_ph=('P23', 'Tooth gem close up'),
         line='A little sparkle for your smile, bonded in minutes with no drilling.',
         intro='A tooth gem is a small crystal bonded to the surface of a tooth. It adds a subtle sparkle to your smile, there is no drilling involved, and it pairs perfectly with a teeth whitening session.',
         what='A small gem is bonded to the front of a clean, dry tooth using an adhesive. No drilling and no damage to the tooth.',
         who='Anyone who wants a fun, subtle accent on their smile, especially after teeth whitening.',
         expect='Pick your gem and placement, the tooth is cleaned and prepped, and the gem is bonded in place. Quick and painless.',
         faqs=[('Does a tooth gem damage your tooth?', 'No drilling is involved. The gem is bonded to the surface of the tooth.'),
               ('How much is a tooth gem?', '[Confirm price and gem options with Brandy.]'),
               ('Can I get a gem with teeth whitening?', 'Yes. Whitening first, then the gem, is the most popular combo.')],
         ba=['P23', 'Tooth gem close up']),
    dict(id='pmu', variant='dax', cat='Smile, brows &amp; lips', slug='brow-color-correction-san-antonio', short='Brow Color Correction', nav='Brow Correction',
         h1='Brow Color Correction &amp; Permanent Makeup in San Antonio',
         title='Brow Color Correction San Antonio | Permanent Makeup | Beautified Studios',
         meta='Brow color correction and permanent makeup in San Antonio. Fix faded, discolored or uneven brows at Beautified Studios. Book online.',
         price='[Price]', dur='[Time]', tag='Permanent makeup', eb_extra=' · Brows gone bad specialist',
         line='Fix faded, discolored or uneven brows and get the shape you wanted.',
         intro='Beautified Studios specializes in permanent makeup, including color correcting and all brows gone bad situations. If old brow tattoos or microblading have turned red, blue or gray, or healed uneven, color correction can neutralize the tone and restore a natural brow.',
         what='Corrective pigment is used to neutralize unwanted tones in old brow work, then the brow is refined to a natural shape and color.',
         who='Clients with old brow tattoos or microblading that has faded, changed color or healed uneven.',
         expect='A consultation to assess your current brows, a color correction plan, then treatment. Some brows need more than one session.',
         faqs=[('Can you fix red, blue or gray brows?', 'Yes. Color correction is used to neutralize those tones. Brandy will assess your brows at your consultation.'),
               ('How many sessions will I need?', 'It depends on how strong the old color is. Some brows need more than one session.'),
               ('Do you do new permanent brows too?', '[Confirm which permanent brow services Brandy offers.]')],
         ba=['P24', 'Brow color correction before and after']),
    dict(id='blush', variant='rha', cat='Smile, brows &amp; lips', slug='lip-blush-san-antonio', short='Lip Blush', nav='Lip Blush',
         h1='Lip Blush Tattoo in San Antonio, TX',
         title='Lip Blush San Antonio | Permanent Lip Color | Beautified Studios',
         meta='Lip blush in San Antonio at Beautified Studios. Soft, long lasting lip color that defines your lips without daily makeup. Book online.',
         price='$575', dur='[Time]', tag='Permanent makeup',
         line='Soft, long lasting color that defines your lips without daily lipstick.',
         intro='Lip blush is a permanent makeup treatment that adds a soft wash of color to the lips. It can define the lip line, even out uneven tone and give you a natural tint that lasts, so you can skip daily lip liner and lipstick.',
         what='Pigment is placed into the lips to add soft color and definition, customized to your skin tone.',
         who='Clients with pale or uneven lip color, or anyone who wants defined lips without daily makeup.',
         expect='A color consultation, numbing, then treatment. Color looks bold at first and softens as it heals.',
         faqs=[('How much is lip blush?', 'Lip blush at Beautified Studios is $575. [Confirm current price.]'),
               ('Lip blush or lip filler?', 'Lip blush adds color and definition. Lip filler adds volume and shape. They pair well together.'),
               ('Does lip blush fade?', 'Permanent makeup softens over time and may need a touch up down the road.')],
         ba=['P25', 'Lip blush before and after']),
]

AREAS = [
    dict(slug='cosmetic-injector-medical-center', name='Medical Center', full='the Medical Center',
         p1='Beautified Studios is in the 78229 ZIP code on Babcock Rd, close to the Medical Center area. If you live or work nearby, a lip flip or Daxxify visit fits easily into a lunch break or the end of your shift.',
         p2='Medical Center clients often book quick treatments like the $150 lip flip or a Perfecting Session, then come back for bigger plans like Full Facial Balancing when they have more time.',
         q=('Is the studio close to the Medical Center?', 'Yes. We are at 1603 Babcock Rd, Suite 230, in the same 78229 ZIP code.')),
    dict(slug='cosmetic-injector-alamo-heights', name='Alamo Heights', full='Alamo Heights',
         p1='Alamo Heights clients choose Beautified Studios for refined, natural looking results. Brandy’s approach is subtle on purpose: enhancements that look like you on your best day.',
         p2='Popular choices with Alamo Heights clients include RHA lip filler, Daxxify for expression lines and Full Facial Balancing for an overall refresh.',
         q=('Do you offer facial balancing for Alamo Heights clients?', 'Yes. Full Facial Balancing is $1,954 and includes three syringes and a complimentary lip flip.')),
    dict(slug='cosmetic-injector-stone-oak', name='Stone Oak', full='Stone Oak',
         p1='From Stone Oak on the north side, Beautified Studios is your San Antonio studio for lip filler, jaw filler, Daxxify and non-surgical nose jobs, all from one Master Injector.',
         p2='Because every appointment starts with a one on one consultation, Stone Oak clients get a plan built around their face, not a menu of one size fits all packages.',
         q=('Is it worth the drive from Stone Oak?', 'Our clients think so. Book online, and if you are coming for jaw filler, a nose job or balancing, plan for about 90 minutes in the chair.')),
    dict(slug='cosmetic-injector-leon-valley', name='Leon Valley', full='Leon Valley',
         p1='Leon Valley clients are just a short trip from Beautified Studios on Babcock Rd. Stop in for a lip flip, Daxxify or a full filler plan with Master Injector Brandy Gonzalez.',
         p2='Not sure where to start? Many Leon Valley clients begin with a $150 lip flip, a subtle first step into injectables.',
         q=('What is the best first treatment?', 'A lip flip is a popular first step: subtle, quick and $150. Brandy will also talk through filler options at your consultation.')),
    dict(slug='cosmetic-injector-helotes', name='Helotes', full='Helotes',
         p1='Clients from Helotes on the northwest side of San Antonio visit Beautified Studios for natural lip filler, sculpted jawlines and smoother expression lines.',
         p2='Brandy specializes in Daxxify and RHA filler, two options many Helotes clients choose for results that look natural in motion.',
         q=('What does Brandy specialize in?', 'Daxxify and RHA filler. She is a Master Injector trained through Monarch Master Injectors.')),
    dict(slug='cosmetic-injector-boerne', name='Boerne', full='Boerne',
         p1='Coming in from Boerne and the Hill Country? Beautified Studios makes the trip worthwhile with treatments that combine several areas in one visit, like Full Facial Balancing.',
         p2='Boerne clients can book online in under a minute, and pay later financing is available in studio for treatments from $50 to $4,000.',
         q=('Can I get several treatments in one trip?', 'Yes. Full Facial Balancing treats multiple areas in one 90 minute visit, which is ideal if you are driving in.')),
]

FAQ_GROUPS = [
    ('Booking &amp; payment', [
        ('How do I book an appointment?', 'Book online any time on our booking page or right on any treatment page. You can also call or text (726) 242-2952.'),
        ('Do I need to pay when I book?', 'You can hold your appointment with a card and pay at your visit, pay in full online, or choose buy now, pay later.'),
        ('What is your cancellation policy?', 'Please give at least 24 hours notice to cancel. Cancellations with less notice are charged 50% of the scheduled service.'),
        ('Do you offer financing?', 'Yes. Buy now, pay later is available in studio for treatments from $50 to $4,000. Get approved before your appointment.'),
    ]),
    ('Treatments', [
        ('What is the difference between a lip flip and lip filler?', 'A lip flip relaxes the muscle above your lip so it rolls slightly outward for a subtle pout. Lip filler adds real volume and shape with RHA filler.'),
        ('What is Daxxify?', 'Daxxify is a wrinkle relaxing injectable, similar to Botox, known for lasting longer between appointments for many clients.'),
        ('What is RHA filler?', 'RHA is a hyaluronic acid filler designed to move with your facial expressions, so results look natural when you talk and smile.'),
        ('Is a non-surgical nose job permanent?', 'No. It uses filler, so results are temporary, with no surgery involved.'),
        ('What is included in Full Facial Balancing?', 'Three syringes of filler placed where your face needs them most plus a complimentary lip flip, for $1,954.'),
        ('What is a Perfecting Session?', 'A follow up visit to fine tune your Botox or filler results.'),
    ]),
    ('Your visit', [
        ('Where is Beautified Studios?', '1603 Babcock Rd, Suite 230, San Antonio, TX 78229.'),
        ('What are your hours?', 'Tuesday 9:00 AM to 6:30 PM, Wednesday to Friday 9:30 AM to 6:00 PM, Saturday 1:30 PM to 5:00 PM. Closed Sunday and Monday.'),
        ('What happens at my first appointment?', 'Every visit starts with a one on one consultation about your goals. Brandy explains your options and pricing before anything begins.'),
        ('Which areas do you serve?', 'Clients visit us from across San Antonio, including the Medical Center, Alamo Heights, Stone Oak, Leon Valley, Helotes and Boerne.'),
    ]),
    ('Smile, brows &amp; lips', [
        ('Do you offer teeth whitening?', 'Yes. In-studio LED teeth whitening, and you can add a tooth gem in the same visit.'),
        ('Can you fix old brow tattoos or microblading?', 'Yes. Beautified Studios specializes in brow color correction and all brows gone bad situations.'),
        ('What is lip blush?', 'Lip blush is permanent makeup that adds soft, long lasting color and definition to your lips.'),
    ]),
    ('Training', [
        ('Do you offer training?', 'Yes. Beautified Studios Academy offers 1:1 courses, including lash and permanent makeup, and Brandy trains injectors through Monarch Master Injectors. See the Academy page.'),
    ]),
]

# ---------- shared parts ----------
def head(title, meta):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="description" content="{meta}">
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{HELMET}
<div style="width: 100%; background: {PAPER}; color: {INK}; font-family: 'Jost', system-ui, sans-serif; font-weight: 400; font-size: 18px; line-height: 1.7">
'''

def tail(props=None, logic=None):
    props = props or {}
    logic = logic or "return {};"
    return f'''</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps(props)}'>
class Component extends DCLogic {{
{logic}
}}
</script>
</body>
</html>
'''

SIMPLE_LOGIC = 'renderVals() {\nreturn {};\n}'

def wordmark(light=False):
    c = PAPER if light else INK
    s = '#E7B9C1' if light else ROSE
    return (f'<a href="Main.dc.html" style="text-decoration: none; color: {c}; display: inline-flex; flex-direction: column; line-height: 1">'
            f'<span class="wm-big" style="{DISP}; font-size: 28px; font-weight: 400; letter-spacing: 0.22em">BEAUTIFIED</span>'
            f'<span class="wm-small" style="font-size: 10px; letter-spacing: 0.72em; margin-top: 7px; color: {s}">STUDIOS</span></a>')

def nav():
    link = f'color: {INK}; text-decoration: none; padding: 12px 0'
    mlink = f'display: block; padding: 16px 0; border-top: 1px solid {LINE}; color: {INK}; text-decoration: none; {DISP}; font-size: 24px'
    links = [('services.dc.html', 'Treatments'), ('about.dc.html', 'About'), ('service-areas.dc.html', 'Areas'), ('faq.dc.html', 'FAQ'), ('academy.dc.html', 'Academy'), ('blog.dc.html', 'Blog'), ('contact.dc.html', 'Contact')]
    desk = ''.join(f'<a href="{h}" style="{link}">{t}</a>' for h, t in links)
    mob = ''.join(f'<a href="{h}" style="{mlink}">{t}</a>' for h, t in links)
    return f'''<div style="background: {WINE}; color: {PAPER}; font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase">
<div style="{WRAP}; padding-top: 10px; padding-bottom: 10px; display: flex; flex-wrap: wrap; gap: 6px 24px; justify-content: space-between">
<span class="tb-addr">{ADDR1} · San Antonio</span>
<span>Tue to Sat · <a href="{TEL}" style="color: {PAPER}; text-decoration: none">{PHONE}</a></span>
</div>
</div>
<header style="position: relative; border-bottom: 1px solid {LINE}; background: {PAPER}">
<nav aria-label="Main" style="{WRAP}; padding-top: 18px; padding-bottom: 18px; display: flex; gap: 16px 40px; align-items: center; justify-content: space-between">
{wordmark()}
<div class="nav-links" style="flex-wrap: wrap; gap: 4px 30px; align-items: center; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase">
{desk}
<a href="{BOOK_URL}" style="{BTN}; padding: 15px 28px">Book now</a>
</div>
<div class="nav-mobile" style="align-items: center; gap: 10px">
<a href="{BOOK_URL}" style="background: {WINE}; color: {PAPER}; text-decoration: none; padding: 12px 18px; border-radius: 999px; font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase">Book</a>
<details>
<summary aria-label="Menu" style="width: 46px; height: 46px; display: flex; align-items: center; justify-content: center; border: 1px solid {LINE}; border-radius: 999px; cursor: pointer"><svg aria-hidden="true" width="20" height="14" viewBox="0 0 20 14" fill="none" stroke="{INK}" stroke-width="1.6"><path d="M0 1h20M0 7h20M0 13h20"></path></svg></summary>
<div style="position: absolute; left: 0; right: 0; top: 100%; z-index: 20; background: {PAPER}; border-bottom: 1px solid {LINE}; padding: 8px 32px 24px; box-shadow: 0 12px 24px rgba(26,19,20,0.08)">
{mob}
<a href="{TEL}" style="display: block; margin-top: 16px; text-align: center; border: 1px solid {INK}; color: {INK}; text-decoration: none; padding: 15px; border-radius: 999px; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase">Call {PHONE}</a>
</div>
</details>
</div>
</nav>
</header>
<a href="lip-filler-san-antonio.dc.html#book" style="display: block; background: {ROSE}; color: #FFFFFF; text-decoration: none; text-align: center; padding: 12px 24px; font-size: 15px; line-height: 1.5"><strong style="font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; font-size: 13px">Limited time</strong> · Complimentary lip flip with purchase of a full syringe of filler ($200 value) · <span style="text-decoration: underline">Book now</span></a>
'''

def crumbs(items):
    parts = []
    for label, href in items:
        if href:
            parts.append(f'<a href="{href}" style="color: {MUTED}; text-decoration: none">{label}</a>')
        else:
            parts.append(f'<span style="color: {INK}">{label}</span>')
    sep = f'<span aria-hidden="true" style="color: {LINE}">/</span>'
    return (f'<nav aria-label="Breadcrumb" style="{WRAP}; padding-top: 28px; display: flex; flex-wrap: wrap; gap: 10px; font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase">'
            + sep.join(parts) + '</nav>')

def footer():
    col = f'display: flex; flex-direction: column; gap: 10px; font-size: 15px'
    lk = 'color: #E9D5D1; text-decoration: none'
    svc_links = ''.join(f'<a href="{s["slug"]}.dc.html" style="{lk}">{s["short"]}</a>' for s in SERVICES)
    area_links = ''.join(f'<a href="{a["slug"]}.dc.html" style="{lk}">{a["name"]}</a>' for a in AREAS)
    head_s = 'margin: 0 0 8px; font-size: 11px; letter-spacing: 0.3em; text-transform: uppercase; color: #E7B9C1'
    return f'''<footer style="background: {WINE}; color: #E9D5D1">
<div style="{WRAP}; padding-top: 88px; padding-bottom: 48px; display: flex; flex-wrap: wrap; gap: 48px 64px; justify-content: space-between">
<div style="flex: 1 1 280px; display: flex; flex-direction: column; gap: 24px">
{wordmark(True)}
<p style="margin: 0; font-size: 15px; max-width: 300px">Cosmetic injector in San Antonio, TX. Lip filler, Daxxify, jaw filler, non-surgical nose jobs and facial balancing.</p>
<p style="margin: 0; font-size: 15px">{ADDR1}<br>{ADDR2}<br><a href="{TEL}" style="{lk}">{PHONE}</a><br><a href="mailto:{EMAIL}" style="{lk}">{EMAIL}</a></p>
</div>
<div style="{col}"><p style="{head_s}">Treatments</p>{svc_links}</div>
<div style="{col}"><p style="{head_s}">Areas we serve</p>{area_links}</div>
<div style="{col}"><p style="{head_s}">Studio</p>
<a href="about.dc.html" style="{lk}">About Brandy</a><a href="academy.dc.html" style="{lk}">Academy</a><a href="faq.dc.html" style="{lk}">FAQ</a><a href="blog.dc.html" style="{lk}">Blog</a><a href="contact.dc.html" style="{lk}">Contact</a><a href="{BOOK_URL}" style="{lk}">Book online</a><a href="{IG}" style="{lk}">Instagram</a><a href="{FB}" style="{lk}">Facebook</a>
</div>
<div style="{col}"><p style="{head_s}">Hours</p>
<span>Tue · 9:00 to 6:30</span><span>Wed to Fri · 9:30 to 6:00</span><span>Sat · 1:30 to 5:00</span><span>Sun &amp; Mon · Closed</span>
</div>
</div>
<div style="{WRAP}; padding-top: 24px; padding-bottom: 32px; border-top: 1px solid #6A3843; display: flex; flex-wrap: wrap; gap: 12px; justify-content: space-between; font-size: 13px; color: #D5BBB6">
<span>© 2026 Beautified Studios · San Antonio, Texas</span>
<span>Results vary. Every treatment begins with a consultation.</span>
</div>
<div aria-hidden="true" style="overflow: hidden; line-height: 0.8; padding-bottom: 12px"><p style="margin: 0; {DISP}; font-size: 17.5vw; letter-spacing: -0.01em; color: #5A2A34; white-space: nowrap; text-align: center">Beautified</p></div>
</footer>
'''

def faq_list(items, dark=False):
    out = []
    for i, (q, a) in enumerate(items):
        bt = f'border-top: 1px solid {LINE}'
        bb = f'; border-bottom: 1px solid {LINE}' if i == len(items) - 1 else ''
        out.append(f'<details style="{bt}{bb}; padding: 26px 0">'
                   f'<summary style="cursor: pointer; display: flex; justify-content: space-between; gap: 24px; align-items: baseline; {DISP}; font-size: 24px; line-height: 1.3"><span>{q}</span><span aria-hidden="true" style="font-family: Jost, sans-serif; font-size: 22px; color: {ROSE}">+</span></summary>'
                   f'<p style="margin: 14px 0 0; color: {MUTED}; max-width: 720px">{a}</p></details>')
    return ''.join(out)

def booking_block(preset='', heading='Book an appointment', sub='Choose what you are booking and pick a time. Brandy confirms by text.'):
    pre = f' preset="{preset}"' if preset else ''
    return f'''<section id="book" style="background: #F1E4E0; border-top: 1px solid {LINE}">
<div style="{WRAP}; padding-top: 104px; padding-bottom: 104px">
<div style="display: flex; flex-wrap: wrap; gap: 16px 48px; justify-content: space-between; align-items: flex-end; margin-bottom: 40px">
<div><p style="{EYEBROW}">Online booking</p><h2 style="{H2}">{heading}</h2></div>
<p style="{P}; max-width: 420px">{sub}</p>
</div>
<dc-import name="Scheduler"{pre} hint-size="100%,940px"></dc-import>
</div>
</section>
'''

def visit_block():
    dirs = 'https://www.google.com/maps/dir/?api=1&amp;destination=1603+Babcock+Rd+Suite+230,+San+Antonio,+TX+78229'
    return f'''<section style="{WRAP}; padding-top: 104px; padding-bottom: 104px">
<div style="display: flex; flex-wrap: wrap; gap: 48px; align-items: stretch">
<div style="flex: 1 1 420px; min-width: 0; display: flex; flex-direction: column; justify-content: space-between; gap: 40px">
<div>
<p style="{EYEBROW}">Location &amp; hours</p>
<h2 style="{H2}">Beautified Studios, San Antonio</h2>
<p style="margin: 28px 0 0; font-size: 20px">{ADDR1}<br>{ADDR2}</p>
<p style="margin: 12px 0 0"><a href="{TEL}" style="color: {INK}">{PHONE}</a> · <a href="mailto:{EMAIL}" style="color: {INK}">{EMAIL}</a></p>
</div>
<div style="display: grid; grid-template-columns: auto 1fr; gap: 10px 40px; font-size: 16px; border-top: 1px solid {LINE}; padding-top: 28px">
<span style="color: {MUTED}">Tuesday</span><span>9:00 AM to 6:30 PM</span>
<span style="color: {MUTED}">Wed to Fri</span><span>9:30 AM to 6:00 PM</span>
<span style="color: {MUTED}">Saturday</span><span>1:30 PM to 5:00 PM</span>
<span style="color: {MUTED}">Sun &amp; Mon</span><span>Closed</span>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 14px"><a href="{BOOK_URL}" style="{BTN}">Book online</a><a href="{dirs}" style="{BTN_O}">Get directions</a></div>
</div>
<div style="flex: 1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
{ph('P16', 'Building entrance &amp; suite sign', 'flex: 1 1 auto; min-height: 300px; border-radius: 4px')}
<div style="display: flex; gap: 16px; flex-wrap: wrap">
{ph('P04', 'Studio interior', 'flex: 1 1 200px; aspect-ratio: 4 / 3; border-radius: 4px')}
{ph('P05', 'Treatment room detail', 'flex: 1 1 200px; aspect-ratio: 4 / 3; border-radius: 4px')}
</div>
</div>
</div>
</section>
'''

def areas_strip():
    links = ''.join(f'<a href="{a["slug"]}.dc.html" style="{DISP}; font-size: clamp(28px, 3.4vw, 46px); color: {PAPER}; text-decoration: none; white-space: nowrap">{a["name"]}</a><span aria-hidden="true" style="{DISP}; font-size: clamp(28px, 3.4vw, 46px); color: #8C5560">/</span>' for a in AREAS)
    return f'''<section style="background: {WINE}; color: {PAPER}">
<div style="{WRAP}; padding-top: 96px; padding-bottom: 96px">
<p style="{EYEBROW_D}">Areas we serve</p>
<div style="display: flex; flex-wrap: wrap; gap: 8px 22px; align-items: baseline">{links}<a href="service-areas.dc.html" style="font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; color: #E7B9C1">All areas</a></div>
</div>
</section>
'''

def service_index(numbered=True):
    def row(n, href, name, line, dur, price, last=False):
        bb = f'; border-bottom: 1px solid {LINE}' if last else ''
        return f'''<a href="{href}" style="display: flex; flex-wrap: wrap; gap: 8px 32px; align-items: baseline; padding: 28px 0; border-top: 1px solid {LINE}{bb}; text-decoration: none; color: {INK}">
<span style="flex: 0 0 56px; {DISP}; font-style: italic; font-size: 20px; color: {ROSE}">{n:02d}</span>
<span style="flex: 1 1 360px; min-width: 0; display: flex; flex-direction: column; gap: 6px"><span style="{DISP}; font-size: clamp(28px, 3.2vw, 44px); line-height: 1.05; letter-spacing: -0.01em">{name}</span><span style="font-size: 15px; color: {MUTED}">{line}</span></span>
<span style="flex: 0 0 auto; display: flex; gap: 28px; align-items: baseline; font-size: 15px"><span style="color: {MUTED}">{dur}</span><span style="font-weight: 500; color: {ROSE}">{price}</span><span aria-hidden="true" style="font-size: 22px">→</span></span>
</a>'''
    out = []; n = 0
    for cat in ['Injectables', 'Smile, brows &amp; lips']:
        out.append(f'<h3 style="margin: 48px 0 8px; font-size: 14px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: {ROSE}">{cat}</h3>')
        items = [x for x in SERVICES if x['cat'] == cat]
        for k, x in enumerate(items):
            n += 1
            out.append(row(n, x['slug'] + '.dc.html', x['short'], x['line'], x['dur'], x['price'], last=(cat != 'Injectables' and k == len(items) - 1)))
        if cat == 'Injectables':
            n += 1
            out.append(row(n, BOOK_URL, 'Perfecting Session', 'A follow up to fine tune your Botox or filler results.', '30 min', 'Priced at consult', last=True))
    return ''.join(out)

FILES = {}

# ---------- HOME ----------
ZONES = [
    dict(id='forehead', num='1', title='Forehead &amp; brows', x='50%', y='22%', tx='Daxxify', price='Priced at consult', copy='Soften frown lines and forehead lines with a longer lasting wrinkle relaxer.', href='daxxify-san-antonio.dc.html'),
    dict(id='nose', num='2', title='Nose', x='50%', y='45%', tx='Non-Surgical Nose Job', price='From $1,500', copy='Smooth a bump and refine your profile with filler. No surgery.', href='non-surgical-nose-job-san-antonio.dc.html'),
    dict(id='cheeks', num='3', title='Cheeks', x='30%', y='50%', tx='RHA Cheek Filler', price='Priced at consult', copy='Restore lift and soft volume to the mid face.', href='lip-filler-san-antonio.dc.html'),
    dict(id='lips', num='4', title='Lips', x='50%', y='63%', tx='Lip Filler or Lip Flip', price='From $150', copy='A subtle flip for $150, or RHA filler for real volume and shape.', href='lip-filler-san-antonio.dc.html'),
    dict(id='jaw', num='5', title='Jawline', x='72%', y='70%', tx='Jaw Filler', price='$1,449', copy='Define the jaw for a sharper, more sculpted profile.', href='jaw-filler-san-antonio.dc.html'),
    dict(id='chin', num='6', title='Chin', x='50%', y='79%', tx='RHA Chin Filler', price='Priced at consult', copy='Bring the chin forward to balance the nose, lips and jaw.', href='lip-filler-san-antonio.dc.html'),
]
zones_js = json.dumps([{k: v.replace('&amp;', '&') for k, v in z.items()} for z in ZONES])

home_logic = '''constructor(props) {
super(props);
this.state = { zone: 'lips' };
}
renderVals() {
var self = this;
var zones = ''' + zones_js + ''';
var cur = zones.filter(function (z) { return z.id === self.state.zone; })[0] || zones[3];
return {
zones: zones.map(function (z) {
var on = z.id === self.state.zone;
return Object.assign({}, z, {
pick: function () { self.setState({ zone: z.id }); },
pinStyle: 'position: absolute; left: ' + z.x + '; top: ' + z.y + '; transform: translate(-50%, -50%); width: 46px; height: 46px; border-radius: 999px; font-family: Jost, sans-serif; font-size: 15px; font-weight: 500; cursor: pointer; ' + (on ? 'background: #4A1F28; color: #F7F0EC; border: 2px solid #F7F0EC; box-shadow: 0 0 0 8px rgba(74,31,40,0.18);' : 'background: #F7F0EC; color: #4A1F28; border: 2px solid #4A1F28;'),
rowStyle: 'display: flex; gap: 16px; align-items: baseline; width: 100%; padding: 16px 0; background: transparent; border: 0; border-top: 1px solid #DCC6C1; font-family: inherit; text-align: left; cursor: pointer; color: ' + (on ? '#4A1F28' : '#463A3C') + ';',
nameStyle: "font-family: 'DM Serif Display', Georgia, serif; font-size: 24px; " + (on ? 'font-style: italic;' : '')
});
}),
cur: cur
};
}'''

home = head('Cosmetic Injector San Antonio | Lip Filler, Daxxify &amp; Facial Balancing | Beautified Studios',
            'Beautified Studios is a San Antonio cosmetic injector studio. Lip filler, lip flips, Daxxify, jaw filler, non-surgical nose jobs and facial balancing by Master Injector Brandy Gonzalez.')
home += nav()
home += f'''
<!-- HERO -->
<section style="{WRAP}; padding-top: 64px; padding-bottom: 72px; display: flex; flex-wrap: wrap; gap: 56px; align-items: stretch">
<div style="flex: 1 1 600px; min-width: 0; display: flex; flex-direction: column; justify-content: space-between; gap: 48px">
<div>
<p style="{EYEBROW}">Beautified Studios · Master Injector Brandy Gonzalez</p>
<h1 style="margin: 0; {DISP}; font-weight: 400; font-size: clamp(56px, 7.4vw, 120px); line-height: 1.02; letter-spacing: -0.01em">Beauty Studio &amp; Injector in <em style="color: {ROSE}">San Antonio, TX</em></h1>
</div>
<div>
<p style="{P}; font-size: 20px; max-width: 600px">Lip filler, Daxxify, jaw filler, facial balancing, teeth whitening, tooth gems, lip blush and brow color correction. Clear prices, financing available, and online booking in about a minute.</p>
<div style="margin-top: 32px; display: flex; flex-wrap: wrap; gap: 14px"><a href="#book" style="{BTN}">Book an appointment</a><a href="services.dc.html" style="{BTN_O}">See all prices</a></div>
<p style="margin: 36px 0 12px; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">Popular treatments</p>
<div style="display: flex; flex-wrap: wrap; gap: 10px">
<a href="lip-flip-san-antonio.dc.html" style="border: 1px solid {LINE}; background: #FFFFFF; border-radius: 999px; padding: 12px 20px; font-size: 15px; color: {INK}; text-decoration: none">Lip Flip · $150</a>
<a href="lip-filler-san-antonio.dc.html" style="border: 1px solid {LINE}; background: #FFFFFF; border-radius: 999px; padding: 12px 20px; font-size: 15px; color: {INK}; text-decoration: none">Lip Filler</a>
<a href="daxxify-san-antonio.dc.html" style="border: 1px solid {LINE}; background: #FFFFFF; border-radius: 999px; padding: 12px 20px; font-size: 15px; color: {INK}; text-decoration: none">Daxxify</a>
<a href="jaw-filler-san-antonio.dc.html" style="border: 1px solid {LINE}; background: #FFFFFF; border-radius: 999px; padding: 12px 20px; font-size: 15px; color: {INK}; text-decoration: none">Jaw Filler · $1,449</a>
<a href="facial-balancing-san-antonio.dc.html" style="border: 1px solid {LINE}; background: #FFFFFF; border-radius: 999px; padding: 12px 20px; font-size: 15px; color: {INK}; text-decoration: none">Facial Balancing · $1,954</a>
<a href="teeth-whitening-san-antonio.dc.html" style="border: 1px solid {LINE}; background: #FFFFFF; border-radius: 999px; padding: 12px 20px; font-size: 15px; color: {INK}; text-decoration: none">Teeth Whitening</a>
<a href="brow-color-correction-san-antonio.dc.html" style="border: 1px solid {LINE}; background: #FFFFFF; border-radius: 999px; padding: 12px 20px; font-size: 15px; color: {INK}; text-decoration: none">Brow Correction</a>
</div>
</div>
</div>
<div style="flex: 1 1 440px; min-width: 0; position: relative; min-height: 640px">
{ph('P01', 'Brandy, editorial portrait', 'position: absolute; top: 0; right: 0; width: 86%; height: 88%; border-radius: 400px 400px 4px 4px')}
{ph('P02', 'Brandy injecting', 'position: absolute; left: 0; bottom: 0; width: 44%; aspect-ratio: 1 / 1; border-radius: 999px; border: 10px solid #F7F0EC')}
<p aria-hidden="true" style="position: absolute; right: -4px; bottom: 0; margin: 0; writing-mode: vertical-rl; transform: rotate(180deg); font-size: 11px; letter-spacing: 0.4em; text-transform: uppercase; color: {ROSE}">10 years in beauty</p>
</div>
</section>

<!-- CREDENTIAL STRIP -->
<section style="border-top: 1px solid {LINE}; border-bottom: 1px solid {LINE}">
<div style="{WRAP}; display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))">
<div style="padding: 28px 24px 28px 0"><p style="margin: 0; {DISP}; font-size: 24px">Master Injector</p><p style="margin: 4px 0 0; font-size: 14px; color: {MUTED}">Trained through Monarch Master Injectors</p></div>
<div style="padding: 28px 24px; border-left: 1px solid {LINE}"><p style="margin: 0; {DISP}; font-size: 24px">Daxxify &amp; RHA Filler</p><p style="margin: 4px 0 0; font-size: 14px; color: {MUTED}">Specialist injector</p></div>
<div style="padding: 28px 24px; border-left: 1px solid {LINE}"><p style="margin: 0; {DISP}; font-size: 24px">Financing Available</p><p style="margin: 4px 0 0; font-size: 14px; color: {MUTED}">Pay later on $50 to $4,000</p></div>
<div style="padding: 28px 24px; border-left: 1px solid {LINE}"><p style="margin: 0; {DISP}; font-size: 24px">Book Online 24/7</p><p style="margin: 4px 0 0; font-size: 14px; color: {MUTED}">Takes about one minute</p></div>
</div>
</section>

''' + booking_block() + f'''
<!-- FACE MAP -->
<section style="{WRAP}; padding-top: 120px; padding-bottom: 120px">
<div style="display: flex; flex-wrap: wrap; gap: 64px; align-items: center">
<div style="flex: 1 1 440px; min-width: 0; max-width: 560px; margin: 0 auto">
<div style="position: relative; width: 100%; aspect-ratio: 4 / 5; background: {BLUSH}; border-radius: 4px">
<span style="position: absolute; left: 20px; bottom: 18px; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: #6E5A5D">P03 · Front facing model portrait</span>
<sc-for list="{{{{zones}}}}" as="z" hint-placeholder-count="6">
<button type="button" onClick="{{{{z.pick}}}}" aria-label="{{{{z.title}}}}" style="{{{{z.pinStyle}}}}">{{{{z.num}}}}</button>
</sc-for>
</div>
</div>
<div style="flex: 1 1 480px; min-width: 0">
<p style="{EYEBROW}">Find your treatment</p>
<h2 style="{H2}">Which area do you want to treat?</h2>
<p style="{P}; margin-top: 20px; max-width: 480px">Tap an area to see the treatment, the price and a link to book.</p>
<div style="margin-top: 36px; display: flex; flex-direction: column">
<sc-for list="{{{{zones}}}}" as="z" hint-placeholder-count="6">
<button type="button" onClick="{{{{z.pick}}}}" style="{{{{z.rowStyle}}}}"><span style="font-size: 13px; width: 24px">{{{{z.num}}}}</span><span style="{{{{z.nameStyle}}}}">{{{{z.title}}}}</span></button>
</sc-for>
</div>
<div style="margin-top: 28px; background: {WINE}; color: {PAPER}; border-radius: 4px; padding: 32px; display: flex; flex-direction: column; gap: 10px">
<p style="margin: 0; font-size: 11px; letter-spacing: 0.3em; text-transform: uppercase; color: #E7B9C1">{{{{cur.title}}}}</p>
<div style="display: flex; flex-wrap: wrap; gap: 8px 24px; justify-content: space-between; align-items: baseline"><p style="margin: 0; {DISP}; font-size: 34px; line-height: 1.1">{{{{cur.tx}}}}</p><p style="margin: 0; font-size: 16px; color: #F2D3D8">{{{{cur.price}}}}</p></div>
<p style="margin: 0; color: #E9D5D1">{{{{cur.copy}}}}</p>
<div style="margin-top: 14px; display: flex; flex-wrap: wrap; gap: 12px"><a href="{{{{cur.href}}}}" style="{BTN_L}; padding: 15px 28px">Treatment details</a><a href="#book" style="display: inline-block; border: 1px solid {PAPER}; color: {PAPER}; text-decoration: none; padding: 14px 28px; border-radius: 999px; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase">Book now</a></div>
</div>
</div>
</div>
</section>

<!-- MENU -->
<section style="{WRAP}; padding-top: 120px; padding-bottom: 120px">
<div style="display: flex; flex-wrap: wrap; gap: 24px 64px; justify-content: space-between; align-items: flex-end; margin-bottom: 48px">
<div><p style="{EYEBROW}">Treatments &amp; prices</p><h2 style="{H2}">Every service, one studio</h2></div>
<p style="{P}; max-width: 400px">Fixed prices are listed. Treatments marked priced at consult depend on how much product you need, and Brandy confirms the price before starting.</p>
</div>
{service_index()}
<div style="margin-top: 40px; background: #F1E4E0; padding: 48px; display: flex; flex-wrap: wrap; gap: 32px; align-items: center; justify-content: space-between">
<div style="flex: 1 1 420px"><p style="{EYEBROW}">Best value</p><p style="margin: 0; {DISP}; font-size: clamp(32px, 3.6vw, 48px); line-height: 1.08">Full Facial Balancing</p><p style="{P}; margin-top: 12px">3 syringes of filler plus a free lip flip in one 90 minute visit.</p></div>
<div style="display: flex; flex-direction: column; gap: 14px; align-items: flex-start"><span style="{DISP}; font-size: 60px; line-height: 1">$1,954</span><a href="facial-balancing-san-antonio.dc.html" style="{BTN}">Book facial balancing</a></div>
</div>
<div style="margin-top: 16px; padding: 22px 0; display: flex; flex-wrap: wrap; gap: 12px 32px; justify-content: space-between; align-items: baseline; border-bottom: 1px dashed #C9A9A6">
<p style="margin: 0; {DISP}; font-style: italic; font-size: 26px">The Secret Service</p>
<p style="margin: 0; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; color: {ROSE}">Ask Brandy for details · <a href="{BOOK_URL}" style="color: {INK}">Book</a></p>
</div>
</section>

<!-- BRANDY -->
<section style="background: #F1E4E0">
<div style="{WRAP}; padding-top: 120px; padding-bottom: 120px; display: flex; flex-wrap: wrap; gap: 64px; align-items: center">
{ph('P06', 'Brandy, candid portrait', 'flex: 1 1 380px; min-width: 0; aspect-ratio: 3 / 4; border-radius: 4px')}
<div style="flex: 1 1 520px; min-width: 0">
<p style="{EYEBROW}">About Brandy Gonzalez</p>
<p style="margin: 0; {DISP}; font-style: italic; font-size: clamp(34px, 4vw, 58px); line-height: 1.12; letter-spacing: -0.01em">“I promise to fulfill any of your beautifying needs.”</p>
<p style="margin: 28px 0 0; font-size: 13px; letter-spacing: 0.26em; text-transform: uppercase">Brandy Gonzalez · Owner &amp; Master Injector</p>
<p style="{P}; margin-top: 24px; max-width: 520px">Brandy Gonzalez owns Beautified Studios in San Antonio. She has 10 years of experience in beauty, is a Master Injector trained through Monarch Master Injectors, and specializes in Daxxify and RHA filler. Every appointment starts with a consultation so you know your plan and price before treatment.</p>
<div style="margin-top: 32px; display: flex; flex-wrap: wrap; gap: 14px"><a href="about.dc.html" style="{BTN_O}">About Brandy</a><a href="academy.dc.html" style="{BTN_O}">Academy</a></div>
</div>
</div>
</section>

<!-- RESULTS -->
<section style="{WRAP}; padding-top: 120px; padding-bottom: 120px">
<div style="display: flex; flex-wrap: wrap; gap: 24px 64px; justify-content: space-between; align-items: flex-end; margin-bottom: 48px">
<div><p style="{EYEBROW}">Real clients</p><h2 style="{H2}">Before &amp; after photos</h2></div>
<a href="{IG}" style="font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; color: {INK}">More on Instagram</a>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 16px">
{ph('P07', 'Lips before / after', 'flex: 2 1 480px; min-height: 620px; border-radius: 4px')}
<div style="flex: 1 1 320px; display: flex; flex-direction: column; gap: 16px">
{ph('P21', 'Lip filler before / during / after', 'flex: 1 1 300px; border-radius: 4px')}
{ph('P17', 'Lip filler result', 'flex: 1 1 300px; border-radius: 4px')}
</div>
</div>
</section>

<!-- REVIEWS -->
<section style="border-top: 1px solid {LINE}">
<div style="{WRAP}; padding-top: 104px; padding-bottom: 104px">
<p style="{EYEBROW}">Client reviews</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 48px">
<figure style="margin: 0; border-top: 1px solid {INK}; padding-top: 28px"><blockquote style="margin: 0; {DISP}; font-style: italic; font-size: 26px; line-height: 1.35">[Paste client review 1 from Google or Instagram]</blockquote><figcaption style="margin-top: 20px; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">[Client first name] · [Treatment]</figcaption></figure>
<figure style="margin: 0; border-top: 1px solid {INK}; padding-top: 28px"><blockquote style="margin: 0; {DISP}; font-style: italic; font-size: 26px; line-height: 1.35">[Paste client review 2]</blockquote><figcaption style="margin-top: 20px; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">[Client first name] · [Treatment]</figcaption></figure>
<figure style="margin: 0; border-top: 1px solid {INK}; padding-top: 28px"><blockquote style="margin: 0; {DISP}; font-style: italic; font-size: 26px; line-height: 1.35">[Paste client review 3]</blockquote><figcaption style="margin-top: 20px; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">[Client first name] · [Treatment]</figcaption></figure>
</div>
</div>
</section>
'''
home += areas_strip()
home += f'''
<!-- FAQ PREVIEW -->
<section style="{WRAP}; padding-top: 120px; padding-bottom: 40px; display: flex; flex-wrap: wrap; gap: 48px 80px">
<div style="flex: 1 1 320px"><p style="{EYEBROW}">Questions</p><h2 style="{H2}">Frequently asked questions</h2><p style="{P}; margin-top: 20px">Pricing, financing, cancellations and first visits.</p><a href="faq.dc.html" style="{BTN_O}; margin-top: 28px">All FAQs</a></div>
<div style="flex: 2 1 560px; min-width: 0">{faq_list([FAQ_GROUPS[1][1][0], FAQ_GROUPS[0][1][3], FAQ_GROUPS[0][1][2], FAQ_GROUPS[2][1][2]])}</div>
</section>
'''
home += visit_block()
home += footer()
home += tail({"$preview": {"width": 1440, "height": 8600}}, home_logic)
FILES['Main.dc.html'] = home

# ---------- SERVICE PAGES (unique layouts) ----------
SCHEMES = {
    'rha':   dict(bg=PAPER, fg=INK, acc=ROSE, sub=MUTED, line=LINE),
    'flip':  dict(bg='#F1E4E0', fg=INK, acc=ROSE, sub=MUTED, line=LINE),
    'dax':   dict(bg=WINE, fg=PAPER, acc='#F2D3D8', sub='#E9D5D1', line='#6A3843'),
    'jaw':   dict(bg=INK, fg=PAPER, acc='#E7B9C1', sub='#D9C9C6', line='#3A2F31'),
    'nose':  dict(bg='#FFFFFF', fg=INK, acc=ROSE, sub=MUTED, line=LINE),
    'teeth': dict(bg='#FFFFFF', fg=INK, acc=ROSE, sub=MUTED, line=LINE),
    'gem':   dict(bg='#F1E4E0', fg=INK, acc=ROSE, sub=MUTED, line=LINE),
    'pmu':   dict(bg=INK, fg=PAPER, acc='#E7B9C1', sub='#D9C9C6', line='#3A2F31'),
    'blush': dict(bg='#F1E4E0', fg=INK, acc=ROSE, sub=MUTED, line=LINE),
    'bal':   dict(bg=ROSE, fg='#FFFFFF', acc='#FFE3E8', sub='#F7E4E7', line='#A9626E'),
}

def btn_for(sc, solid=True):
    if sc['bg'] in (WINE, INK, ROSE):
        return BTN_L if solid else f'display: inline-block; border: 1px solid {sc["fg"]}; color: {sc["fg"]}; text-decoration: none; padding: 17px 32px; border-radius: 999px; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase'
    return BTN if solid else BTN_O

def facts(s, sc):
    cell = 'flex: 1 1 150px; padding: 18px 20px 18px 0'
    lab = f'margin: 0; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {sc["sub"]}'
    val = f'margin: 4px 0 0; {DISP}; font-size: 26px; color: {sc["fg"]}'
    return (f'<div style="display: flex; flex-wrap: wrap; border-top: 1px solid {sc["line"]}; border-bottom: 1px solid {sc["line"]}">'
            f'<div style="{cell}"><p style="{lab}">Price</p><p style="{val}">{s["price"]}</p></div>'
            f'<div style="{cell}"><p style="{lab}">Appointment</p><p style="{val}">{s["dur"]}</p></div>'
            f'<div style="{cell}"><p style="{lab}">Financing</p><p style="{val}">Available</p></div></div>')

def h1s(size='clamp(48px, 6.4vw, 96px)', color=INK, align='left'):
    return f'margin: 0; {DISP}; font-weight: 400; font-size: {size}; line-height: 1.04; letter-spacing: -0.01em; color: {color}; text-align: {align}'

def service_hero(s):
    sc = SCHEMES[s['id']]
    cta = f'<div style="margin-top: 28px; display: flex; flex-wrap: wrap; gap: 14px"><a href="#book" style="{btn_for(sc)}">Book {s["nav"]}</a><a href="{TEL}" style="{btn_for(sc, False)}">Call {PHONE}</a></div>'
    eb = f'margin: 0 0 18px; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {sc["acc"]}'
    lead = f'margin: 24px 0 0; font-size: 20px; color: {sc["sub"]}; max-width: 560px'
    i = s.get('variant', s['id'])
    if i == 'rha':  # split, arch photo right
        return f'''<section style="background: {sc['bg']}"><div style="{WRAP}; padding-top: 48px; padding-bottom: 96px; display: flex; flex-wrap: wrap; gap: 56px; align-items: center">
<div style="flex: 1 1 560px; min-width: 0"><p style="{eb}">{s['tag']}</p><h1 style="{h1s()}">{s['h1']}</h1><p style="{lead}">{s['line']}</p><div style="margin-top: 36px">{facts(s, sc)}</div>{cta}</div>
{ph(s['ba'][0], s['ba'][1], 'flex: 1 1 420px; min-width: 0; min-height: 620px; border-radius: 400px 400px 4px 4px')}
</div></section>'''
    if i == 'flip':  # centered, giant price
        return f'''<section style="background: {sc['bg']}"><div style="{WRAP}; padding-top: 64px; padding-bottom: 88px; text-align: center">
<p style="{eb}">{s['tag']} · {s['dur']}</p><h1 style="{h1s(align='center')}">{s['h1']}</h1>
<p style="margin: 8px 0 0; {DISP}; font-size: clamp(120px, 18vw, 260px); line-height: 1; letter-spacing: -0.01em; color: {ROSE}">{s.get('big', '$150')}</p>
<p style="{lead}; margin-left: auto; margin-right: auto">{s['line']}{' One flat price, no surprises.' if s['id'] == 'flip' else ''}</p>
<div style="margin-top: 32px; display: flex; flex-wrap: wrap; gap: 14px; justify-content: center"><a href="#book" style="{BTN}">Book {s['nav']}</a><a href="{s.get('compare', ('#compare', 'Lip flip vs filler'))[0]}" style="{BTN_O}">{s.get('compare', ('#compare', 'Lip flip vs filler'))[1]}</a></div>
<div style="margin-top: 64px; display: flex; flex-wrap: wrap; gap: 16px">{ph(s['ba'][0], 'Before', 'flex: 1 1 280px; aspect-ratio: 1 / 1; border-radius: 4px')}{ph(s['ba'][0], 'After', 'flex: 1 1 280px; aspect-ratio: 1 / 1; border-radius: 4px')}{ph(s.get('extra_ph', ('P17', 'Lips close up'))[0], s.get('extra_ph', ('P17', 'Lips close up'))[1], 'flex: 1 1 280px; aspect-ratio: 1 / 1; border-radius: 4px')}</div>
</div></section>'''
    if i == 'dax':  # dark, circle photo
        return f'''<section style="background: {sc['bg']}; color: {sc['fg']}"><div style="{WRAP}; padding-top: 72px; padding-bottom: 104px; display: flex; flex-wrap: wrap; gap: 64px; align-items: center">
{ph(s['ba'][0], s['ba'][1], 'flex: 0 1 460px; min-width: 280px; aspect-ratio: 1 / 1; border-radius: 999px; margin: 0 auto')}
<div style="flex: 1 1 520px; min-width: 0"><p style="{eb}">{s['tag']}{s.get('eb_extra', ' · Daxxify specialist')}</p><h1 style="{h1s(color=PAPER)}">{s['h1']}</h1><p style="{lead}">{s['line']}</p><div style="margin-top: 36px">{facts(s, sc)}</div>{cta}</div>
</div></section>'''
    if i == 'jaw':  # full width photo with overlay card
        return f'''<section style="background: {sc['bg']}; color: {sc['fg']}"><div style="{WRAP}; padding-top: 40px; padding-bottom: 96px">
<div style="position: relative">
{ph(s['ba'][0], s['ba'][1], 'width: 100%; min-height: 640px; border-radius: 4px')}
<div class="ov-card" style="position: absolute; left: 32px; bottom: 32px; max-width: 620px; background: {INK}; padding: 44px; box-sizing: border-box; margin-right: 32px">
<p style="{eb}">{s['tag']}</p><h1 style="{h1s('clamp(44px, 5.4vw, 80px)', PAPER)}">{s['h1']}</h1><p style="{lead}">{s['line']}</p>{cta}
</div></div>
<div style="margin-top: 40px">{facts(s, sc)}</div>
</div></section>'''
    if i == 'nose':  # before/after split hero
        return f'''<section style="background: {sc['bg']}"><div style="{WRAP}; padding-top: 48px; padding-bottom: 96px">
<div style="display: flex; flex-wrap: wrap; gap: 24px 64px; align-items: flex-end; margin-bottom: 48px">
<h1 style="flex: 2 1 600px; {h1s()}">{s['h1']}</h1>
<div style="flex: 1 1 340px"><p style="{eb}">{s['tag']}</p><p style="{P}; font-size: 19px">{s['line']}</p>{cta}</div>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 4px">
{ph(s['ba'][0], s.get('ba_labels', ('Before · side profile', 'After · side profile'))[0], 'flex: 1 1 420px; min-height: 520px')}
{ph(s['ba'][0], s.get('ba_labels', ('Before · side profile', 'After · side profile'))[1], 'flex: 1 1 420px; min-height: 520px; background: #E3CBC6')}
</div>
<div style="margin-top: 40px">{facts(s, sc)}</div>
</div></section>'''
    if i == 'bal':  # rose bg, receipt card
        items = [('3 syringes of RHA filler', 'Placed where your face needs them'), ('Complimentary lip flip', 'A $150 value, included'), ('Full facial assessment', 'Your plan approved before treatment'), ('90 minute appointment', 'Several areas, one visit')]
        rows = ''.join(f'<div style="display: flex; justify-content: space-between; gap: 16px; padding: 16px 0; border-top: 1px dashed {LINE}"><span style="display: flex; flex-direction: column"><span style="font-size: 17px; color: {INK}">{a}</span><span style="font-size: 14px; color: {MUTED}">{b}</span></span><span aria-hidden="true" style="color: {ROSE}">✓</span></div>' for a, b in items)
        return f'''<section style="background: {sc['bg']}; color: {sc['fg']}"><div style="{WRAP}; padding-top: 72px; padding-bottom: 104px; display: flex; flex-wrap: wrap; gap: 64px; align-items: center">
<div style="flex: 1 1 520px; min-width: 0"><p style="{eb}">{s['tag']}</p><h1 style="{h1s(color='#FFFFFF')}">{s['h1']}</h1><p style="{lead}">{s['line']}</p>{cta}</div>
<div style="flex: 1 1 400px; min-width: 0; background: {PAPER}; color: {INK}; padding: 40px; box-sizing: border-box; border-radius: 4px">
<p style="margin: 0; font-size: 11px; letter-spacing: 0.3em; text-transform: uppercase; color: {ROSE}">What is included</p>
<div style="margin-top: 18px">{rows}</div>
<div style="display: flex; justify-content: space-between; align-items: baseline; padding-top: 20px; border-top: 2px solid {INK}"><span style="font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase">Total</span><span style="{DISP}; font-size: 52px; line-height: 1">$1,954</span></div>
<p style="margin: 12px 0 0; font-size: 14px; color: {MUTED}">Pay later financing available in studio.</p>
</div>
</div></section>'''

def compare_table(cols, rows):
    head = ''.join(f'<th scope="col" style="text-align: left; padding: 18px 20px; {DISP}; font-weight: 400; font-size: 26px; border-bottom: 2px solid {INK}">{c}</th>' for c in cols)
    body = ''
    for r in rows:
        body += '<tr>' + f'<th scope="row" style="text-align: left; padding: 18px 20px 18px 0; font-size: 12px; letter-spacing: 0.2em; text-transform: uppercase; color: {MUTED}; font-weight: 500; border-bottom: 1px solid {LINE}; vertical-align: top">{r[0]}</th>' + ''.join(f'<td style="padding: 18px 20px; border-bottom: 1px solid {LINE}; vertical-align: top">{c}</td>' for c in r[1:]) + '</tr>'
    return f'<div style="overflow-x: auto"><table style="width: 100%; min-width: 620px; border-collapse: collapse; font-size: 16px"><thead><tr><th scope="col" style="border-bottom: 2px solid {INK}"></th>{head}</tr></thead><tbody>{body}</tbody></table></div>'

def unique_section(s):
    i = s['id']
    if i == 'teeth':
        return f'''<section style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><div style="background: {WINE}; color: {PAPER}; padding: 56px; display: flex; flex-wrap: wrap; gap: 40px; align-items: center; border-radius: 4px">
<div style="flex: 1 1 460px"><p style="{EYEBROW_D}">Most popular combo</p><h2 style="{H2}; color: {PAPER}">Whitening + a tooth gem</h2><p style="margin: 18px 0 0; color: #E9D5D1; font-size: 18px">Brighten first, then add a gem for a little sparkle. Both in one visit.</p></div>
{ph('P23', 'Tooth gem close up', 'flex: 1 1 320px; aspect-ratio: 4 / 3; border-radius: 4px')}
<a href="tooth-gems-san-antonio.dc.html" style="{BTN_L}">See tooth gems</a></div></section>'''
    if i == 'gem':
        st = [('01', 'Choose', 'Pick your gem and where you want it.'), ('02', 'Prep', 'The tooth surface is cleaned and dried.'), ('03', 'Bond', 'The gem is bonded in place. No drilling.')]
        c = ''.join(f'<div style="flex: 1 1 260px; border-top: 1px solid {INK}; padding-top: 24px"><p style="margin: 0; {DISP}; font-style: italic; font-size: 20px; color: {ROSE}">{n}</p><h3 style="{H3}; margin-top: 8px">{t}</h3><p style="{P}; margin-top: 10px">{d}</p></div>' for n, t, d in st)
        return f'<section id="how" style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><p style="{EYEBROW}">How it works</p><h2 style="{H2}; margin-bottom: 48px">Three quick steps</h2><div style="display: flex; flex-wrap: wrap; gap: 32px">{c}</div><p style="{P}; margin-top: 28px">[Confirm gem options and pricing with Brandy.]</p></section>'
    if i == 'pmu':
        fixes = [('Red or pink brows', 'Old pigment that healed warm.'), ('Blue or gray brows', 'Cool tones from aged tattoo ink.'), ('Faded, patchy brows', 'Microblading that did not hold evenly.'), ('Uneven shape', 'Brows that healed too thick, thin or lopsided.')]
        c = ''.join(f'<div style="flex: 1 1 260px; background: {PAPER}; padding: 28px; border-radius: 4px"><h3 style="{H3}">{t}</h3><p style="{P}; margin-top: 10px">{d}</p></div>' for t, d in fixes)
        return f'<section style="background: #F1E4E0"><div style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><p style="{EYEBROW}">Brows gone bad?</p><h2 style="{H2}; margin-bottom: 48px">What color correction can fix</h2><div style="display: flex; flex-wrap: wrap; gap: 16px">{c}</div></div></section>'
    if i == 'blush':
        t = compare_table(['Lip Blush', 'Lip Filler'], [
            ('What it does', 'Adds soft color and definition', 'Adds volume and shape'),
            ('Method', 'Permanent makeup pigment', 'RHA filler injection'),
            ('Price', '$575', 'Priced at consult'),
            ('Best for', 'Pale or uneven lip color', 'Thin lips or uneven shape')])
        return f'<section style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><p style="{EYEBROW}">Compare</p><h2 style="{H2}; margin-bottom: 40px">Lip blush vs. lip filler</h2>{t}<p style="{P}; margin-top: 24px">Want both color and volume? They pair well. <a href="lip-filler-san-antonio.dc.html" style="color: {INK}">See lip filler</a>.</p></section>'
    if i == 'rha':
        cards = [('Lips', 'Volume, shape and a defined border.', 'P21'), ('Chin', 'Bring the chin forward to balance your profile.', 'P19'), ('Cheeks', 'Lift and soft volume in the mid face.', 'P20')]
        c = ''.join(f'<div style="flex: 1 1 300px; min-width: 0; display: flex; flex-direction: column; gap: 16px">{ph(code, t + " filler result", "aspect-ratio: 4 / 5; border-radius: 4px")}<h3 style="{H3}">{t} filler</h3><p style="{P}">{d}</p></div>' for t, d, code in cards)
        return f'<section style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><p style="{EYEBROW}">Three areas, one filler</p><h2 style="{H2}; margin-bottom: 48px">Lips, chin or cheeks</h2><div style="display: flex; flex-wrap: wrap; gap: 32px">{c}</div></section>'
    if i == 'flip':
        t = compare_table(['Lip Flip', 'Lip Filler'], [
            ('What it does', 'Rolls the upper lip slightly outward', 'Adds real volume and shape'),
            ('Product', 'Wrinkle relaxer', 'RHA filler'),
            ('Price', '$150', 'Priced at consult'),
            ('Best for', 'First timers and subtle changes', 'Noticeably fuller lips'),
            ('Appointment', '60 minutes', '60 minutes')])
        return f'<section id="compare" style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><p style="{EYEBROW}">Compare</p><h2 style="{H2}; margin-bottom: 40px">Lip flip vs. lip filler</h2>{t}<p style="{P}; margin-top: 24px">Not sure? Book a lip flip and ask Brandy about filler at your visit. <a href="lip-filler-san-antonio.dc.html" style="color: {INK}">See lip filler</a>.</p></section>'
    if i == 'dax':
        t = compare_table(['Daxxify', 'Traditional Botox'], [
            ('How it works', 'Relaxes the muscles behind expression lines', 'Relaxes the muscles behind expression lines'),
            ('Known for', 'Lasting longer between visits for many clients', 'The most familiar name'),
            ('Common areas', 'Frown lines, forehead lines', 'Frown lines, forehead lines'),
            ('At Beautified', 'Specialist treatment, priced at consult', 'Ask Brandy')])
        return f'<section style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><p style="{EYEBROW}">Compare</p><h2 style="{H2}; margin-bottom: 40px">Daxxify vs. Botox</h2>{t}</section>'
    if i == 'jaw':
        c = ''.join(ph('P08', a, 'flex: 1 1 300px; aspect-ratio: 3 / 4; border-radius: 4px') for a in ['Front view', 'Three quarter view', 'Side profile'])
        return f'<section style="background: {INK}; color: {PAPER}"><div style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><p style="{EYEBROW_D}">Every angle</p><h2 style="{H2}; color: {PAPER}; margin-bottom: 48px">Jawline results from the front, side and three quarter view</h2><div style="display: flex; flex-wrap: wrap; gap: 16px">{c}</div></div></section>'
    if i == 'nose':
        can = ['Smooth a bump on the bridge', 'Straighten the look of the nose', 'Lift a drooping tip', 'Even out dips and asymmetry']
        cant = ['Make the nose smaller', 'Fix breathing problems', 'Give permanent results', 'Replace surgery in every case']
        li = lambda xs, mark: ''.join(f'<li style="display: flex; gap: 14px; padding: 16px 0; border-top: 1px solid {LINE}; font-size: 18px"><span aria-hidden="true" style="color: {ROSE}; width: 18px">{mark}</span>{x}</li>' for x in xs)
        return f'''<section style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><p style="{EYEBROW}">Set the right expectations</p><h2 style="{H2}; margin-bottom: 48px">What a non-surgical nose job can and cannot do</h2>
<div style="display: flex; flex-wrap: wrap; gap: 48px"><div style="flex: 1 1 360px"><h3 style="{H3}; margin-bottom: 12px">It can</h3><ul style="list-style: none; margin: 0; padding: 0">{li(can, '✓')}</ul></div><div style="flex: 1 1 360px"><h3 style="{H3}; margin-bottom: 12px">It cannot</h3><ul style="list-style: none; margin: 0; padding: 0">{li(cant, '×')}</ul></div></div></section>'''
    if i == 'bal':
        areas = ['Lips', 'Chin', 'Jawline', 'Cheeks', 'Lip flip']
        chips = ''.join(f'<span style="{DISP}; font-size: clamp(36px, 4.4vw, 64px); line-height: 1.1">{a}</span><span aria-hidden="true" style="{DISP}; font-size: clamp(36px, 4.4vw, 64px); color: {ROSE}">+</span>' for a in areas[:-1]) + f'<span style="{DISP}; font-size: clamp(36px, 4.4vw, 64px); font-style: italic; color: {ROSE}">{areas[-1]}</span>'
        return f'<section style="{WRAP}; padding-top: 104px; padding-bottom: 104px"><p style="{EYEBROW}">Areas commonly treated</p><div style="display: flex; flex-wrap: wrap; gap: 4px 20px; align-items: baseline">{chips}</div><p style="{P}; margin-top: 28px; max-width: 620px">Brandy decides where your three syringes go after assessing your face. Most plans combine two to four of these areas.</p></section>'

for s in SERVICES:
    others = [o for o in SERVICES if o['id'] != s['id']][:3]
    rel = ''.join(f'''<a href="{o['slug']}.dc.html" style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 10px; padding: 28px 0; border-top: 1px solid {INK}; text-decoration: none; color: {INK}"><span style="{DISP}; font-size: 30px">{o['short']}</span><span style="font-size: 15px; color: {MUTED}">{o['line']}</span><span style="font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; color: {ROSE}">{o['price']} →</span></a>''' for o in others)
    area_chips = ''.join(f'<a href="{a["slug"]}.dc.html" style="border: 1px solid {LINE}; border-radius: 999px; padding: 12px 20px; font-size: 14px; color: {INK}; text-decoration: none">{s["nav"]} near {a["name"]}</a>' for a in AREAS)
    steps = [('01', 'How it works', s['what']), ('02', 'Who it is for', s['who']), ('03', 'Your appointment', s['expect'])]
    steps_html = ''.join(f'<div style="border-top: 1px solid {INK}; padding-top: 24px"><p style="margin: 0; {DISP}; font-style: italic; font-size: 20px; color: {ROSE}">{n}</p><h3 style="{H3}; margin-top: 10px">{t}</h3><p style="{P}; margin-top: 12px">{c}</p></div>' for n, t, c in steps)
    sc = SCHEMES[s['id']]
    page = head(s['title'], s['meta'])
    page += nav()
    page += f'<div style="background: {sc["bg"]}">' + crumbs([('Home', 'Main.dc.html'), ('Treatments', 'services.dc.html'), (s['short'], None)]).replace(f'color: {MUTED}; text-decoration: none', f'color: {sc["sub"]}; text-decoration: none').replace(f'<span style="color: {INK}">', f'<span style="color: {sc["fg"]}">') + '</div>'
    page += service_hero(s)
    page += f'''
<section style="background: #F1E4E0">
<div style="{WRAP}; padding-top: 104px; padding-bottom: 104px">
<div style="display: flex; flex-wrap: wrap; gap: 32px 80px; margin-bottom: 64px">
<h2 style="{H2}; flex: 1 1 360px">What is {s['nav']}?</h2>
<p style="{P}; flex: 1 1 480px; font-size: 19px">{s['intro']}</p>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px">{steps_html}</div>
</div>
</section>
'''
    page += unique_section(s)
    page += booking_block(s['id'], f'Book {s["nav"]} in San Antonio', f'{s["short"]} is already selected. Just pick a time.')
    page += f'''
<section style="{WRAP}; padding-top: 104px; padding-bottom: 72px; display: flex; flex-wrap: wrap; gap: 48px 80px">
<div style="flex: 1 1 320px"><p style="{EYEBROW}">Questions</p><h2 style="{H2}">{s['nav']} questions</h2></div>
<div style="flex: 2 1 560px; min-width: 0">{faq_list(s['faqs'])}</div>
</section>
<section style="{WRAP}; padding-top: 40px; padding-bottom: 72px">
<p style="{EYEBROW}">Related treatments</p>
<div style="display: flex; flex-wrap: wrap; gap: 0 40px">{rel}</div>
</section>
<section style="{WRAP}; padding-bottom: 104px">
<p style="{EYEBROW}">{s['nav']} near you in San Antonio</p>
<div style="display: flex; flex-wrap: wrap; gap: 10px">{area_chips}</div>
</section>
'''
    page += footer()
    page += tail({"$preview": {"width": 1440, "height": 5800}}, SIMPLE_LOGIC)
    FILES[f"{s['slug']}.dc.html"] = page

# ---------- AREA PAGES (unique layouts) ----------
FEATURE = {'cosmetic-injector-medical-center': 'flip', 'cosmetic-injector-alamo-heights': 'dax', 'cosmetic-injector-stone-oak': 'jaw',
           'cosmetic-injector-leon-valley': 'rha', 'cosmetic-injector-helotes': 'nose', 'cosmetic-injector-boerne': 'bal'}
FEATURE_WHY = {
    'flip': 'Quick, $150 and done in about an hour. The most popular choice for Medical Center clients booking around work.',
    'dax': 'Fewer appointments to keep your results, which is why Daxxify is a favorite with Alamo Heights clients.',
    'jaw': 'A defined, sculpted jawline in one 90 minute visit, the most requested contouring treatment from Stone Oak.',
    'rha': 'Natural looking volume for lips, chin or cheeks with RHA filler, a go to for Leon Valley clients.',
    'nose': 'Smooth and straighten your profile without surgery, a top request from Helotes clients.',
    'bal': 'Several areas treated in one 90 minute visit, ideal when you are driving in from Boerne.',
}
AREA_STYLE = {
    'cosmetic-injector-medical-center': 'darkcard',
    'cosmetic-injector-alamo-heights': 'centered',
    'cosmetic-injector-stone-oak': 'photo',
    'cosmetic-injector-leon-valley': 'stats',
    'cosmetic-injector-helotes': 'map',
    'cosmetic-injector-boerne': 'rose',
}

def area_hero(a, dirs):
    st = AREA_STYLE[a['slug']]
    name = a['name']
    h1 = f'Lip Filler &amp; Injectables Near <em style="font-style: italic">{name}</em>'
    addr_card = lambda bg, fg, sub: f'''<div style="background: {bg}; color: {fg}; padding: 36px; border-radius: 4px; box-sizing: border-box"><p style="margin: 0; font-size: 11px; letter-spacing: 0.3em; text-transform: uppercase; color: {sub}">Studio for {name} clients</p><p style="margin: 14px 0 0; {DISP}; font-size: 28px; line-height: 1.2">{ADDR1}<br>{ADDR2}</p><p style="margin: 14px 0 0; color: {sub}">Tue to Sat · {PHONE}</p><a href="{dirs}" style="display: inline-block; margin-top: 20px; color: {fg}; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase">Directions from {name} →</a></div>'''
    if st == 'darkcard':
        return f'''<section style="background: {WINE}; color: {PAPER}"><div style="{WRAP}; padding-top: 72px; padding-bottom: 96px; display: flex; flex-wrap: wrap; gap: 56px; align-items: center">
<div style="flex: 2 1 600px; min-width: 0"><p style="{EYEBROW_D}">Serving {a['full']}</p><h1 style="{h1s('clamp(48px, 6.4vw, 100px)', PAPER)}">{h1}</h1><p style="margin: 24px 0 0; font-size: 19px; color: #E9D5D1; max-width: 560px">{a['p1']}</p><div style="margin-top: 28px"><a href="#book" style="{BTN_L}">Book now</a></div></div>
<div style="flex: 1 1 340px; min-width: 0">{addr_card(PAPER, INK, MUTED)}</div></div></section>'''
    if st == 'centered':
        chips = ''.join(f'<a href="{s["slug"]}.dc.html" style="border: 1px solid {LINE}; background: #FFFFFF; border-radius: 999px; padding: 12px 20px; font-size: 15px; color: {INK}; text-decoration: none">{s["nav"]} · {s["price"]}</a>' for s in SERVICES)
        return f'''<section style="{WRAP}; padding-top: 88px; padding-bottom: 88px; text-align: center"><p style="{EYEBROW}">Serving {a['full']}</p><h1 style="{h1s('clamp(52px, 7.4vw, 120px)', INK, 'center')}">{h1}</h1><p style="{P}; font-size: 19px; max-width: 620px; margin: 24px auto 0">{a['p1']}</p>
<div style="margin-top: 36px; display: flex; flex-wrap: wrap; gap: 10px; justify-content: center">{chips}</div><div style="margin-top: 32px; display: flex; flex-wrap: wrap; gap: 14px; justify-content: center"><a href="#book" style="{BTN}">Book now</a><a href="{dirs}" style="{BTN_O}">Directions from {name}</a></div></section>'''
    if st == 'photo':
        return f'''<section style="{WRAP}; padding-top: 40px; padding-bottom: 96px"><div style="display: flex; flex-wrap: wrap; gap: 0">
{ph('P04', 'Studio interior', 'flex: 1 1 520px; min-height: 600px')}
<div style="flex: 1 1 460px; min-width: 0; background: {INK}; color: {PAPER}; padding: 56px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center"><p style="{EYEBROW_D}">Serving {a['full']}</p><h1 style="{h1s('clamp(44px, 5vw, 76px)', PAPER)}">{h1}</h1><p style="margin: 24px 0 0; font-size: 18px; color: #D9C9C6">{a['p1']}</p><div style="margin-top: 28px; display: flex; flex-wrap: wrap; gap: 14px"><a href="#book" style="{BTN_L}">Book now</a><a href="{dirs}" style="display: inline-block; border: 1px solid {PAPER}; color: {PAPER}; text-decoration: none; padding: 17px 32px; border-radius: 999px; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase">Directions</a></div></div>
</div></section>'''
    if st == 'stats':
        stat = lambda big, small: f'<div style="flex: 1 1 200px; border-top: 1px solid {INK}; padding-top: 20px"><p style="margin: 0; {DISP}; font-size: 52px; line-height: 1">{big}</p><p style="margin: 8px 0 0; font-size: 14px; color: {MUTED}">{small}</p></div>'
        return f'''<section style="background: #F1E4E0"><div style="{WRAP}; padding-top: 72px; padding-bottom: 88px"><p style="{EYEBROW}">Serving {a['full']}</p><h1 style="{h1s('clamp(52px, 7vw, 112px)')}; max-width: 1000px">{h1}</h1>
<div style="margin-top: 48px; display: flex; flex-wrap: wrap; gap: 24px 40px">{stat('$150', 'Lip flip, our most popular first treatment')}{stat('10 yrs', 'Brandy’s experience in beauty')}{stat('$50–$4k', 'Range eligible for pay later financing')}{stat('1 min', 'To book online')}</div>
<div style="margin-top: 40px; display: flex; flex-wrap: wrap; gap: 14px; align-items: center"><a href="#book" style="{BTN}">Book now</a><a href="{dirs}" style="{BTN_O}">Directions from {name}</a></div></div></section>'''
    if st == 'map':
        return f'''<section style="{WRAP}; padding-top: 48px; padding-bottom: 96px"><div style="position: relative">
{ph('MAP', f'Map: {name} to 1603 Babcock Rd', 'width: 100%; min-height: 560px; border-radius: 4px; background: #E8DCD8')}
<div class="ov-card" style="position: absolute; top: 32px; left: 32px; right: 32px; max-width: 640px; background: {PAPER}; padding: 44px; box-sizing: border-box; border-radius: 4px"><p style="{EYEBROW}">Serving {a['full']}</p><h1 style="{h1s('clamp(40px, 4.8vw, 72px)')}">{h1}</h1><p style="{P}; margin-top: 18px">{a['p1']}</p><div style="margin-top: 24px; display: flex; flex-wrap: wrap; gap: 14px"><a href="#book" style="{BTN}">Book now</a><a href="{dirs}" style="{BTN_O}">Get directions</a></div></div>
</div></section>'''
    if st == 'rose':
        return f'''<section style="background: {ROSE}; color: #FFFFFF"><div style="{WRAP}; padding-top: 72px; padding-bottom: 96px; display: flex; flex-wrap: wrap; gap: 56px; align-items: flex-end">
<div style="flex: 2 1 640px; min-width: 0"><p style="margin: 0 0 18px; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: #FFE3E8">Serving {a['full']} &amp; the Hill Country</p><h1 style="{h1s('clamp(52px, 7vw, 112px)', '#FFFFFF')}">{h1}</h1></div>
<div style="flex: 1 1 340px; min-width: 0"><p style="margin: 0; font-size: 19px; color: #F7E4E7">{a['p1']}</p><div style="margin-top: 28px; display: flex; flex-wrap: wrap; gap: 14px"><a href="#book" style="{BTN_L}">Book now</a><a href="{dirs}" style="display: inline-block; border: 1px solid #FFFFFF; color: #FFFFFF; text-decoration: none; padding: 17px 32px; border-radius: 999px; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase">Directions</a></div></div>
</div></section>'''

for a in AREAS:
    origin = a['name'].replace(' ', '+') + ',+San+Antonio,+TX' if a['name'] != 'Boerne' else 'Boerne,+TX'
    dirs = f'https://www.google.com/maps/dir/?api=1&amp;origin={origin}&amp;destination=1603+Babcock+Rd+Suite+230,+San+Antonio,+TX+78229'
    feat = [s for s in SERVICES if s['id'] == FEATURE[a['slug']]][0]
    rest = [s for s in SERVICES if s['id'] != feat['id']]
    svc_rows = ''.join(f'''<a href="{s['slug']}.dc.html" style="display: flex; flex-wrap: wrap; gap: 6px 24px; justify-content: space-between; align-items: baseline; padding: 22px 0; border-top: 1px solid {LINE}; text-decoration: none; color: {INK}"><span style="{DISP}; font-size: 26px">{s['short']}</span><span style="font-size: 15px; color: {ROSE}">{s['price']} →</span></a>''' for s in rest)
    other = ''.join(f'<a href="{o["slug"]}.dc.html" style="border: 1px solid {LINE}; border-radius: 999px; padding: 12px 20px; font-size: 14px; color: {INK}; text-decoration: none">{o["name"]}</a>' for o in AREAS if o['slug'] != a['slug'])
    faqs = [a['q'],
            (f'Can I book online from {a["name"]}?', 'Yes. Book any time on this page. Pick your treatment, time and how you want to pay in about a minute.'),
            ('What are your hours?', 'Tuesday 9:00 AM to 6:30 PM, Wednesday to Friday 9:30 AM to 6:00 PM and Saturday 1:30 PM to 5:00 PM.')]
    page = head(f'Cosmetic Injector Near {a["name"]}, San Antonio | Lip Filler &amp; Daxxify | Beautified Studios',
                f'Lip filler, Daxxify, jaw filler and facial balancing for {a["name"]} clients. Beautified Studios, 1603 Babcock Rd, San Antonio. Book online.')
    page += nav()
    page += crumbs([('Home', 'Main.dc.html'), ('Areas we serve', 'service-areas.dc.html'), (a['name'], None)])
    page += area_hero(a, dirs)
    page += f'''
<section style="{WRAP}; padding-top: 104px; padding-bottom: 104px; display: flex; flex-wrap: wrap; gap: 48px 80px; align-items: flex-start">
<div style="flex: 1 1 460px; min-width: 0">
<p style="{EYEBROW}">Most booked by {a['name']} clients</p>
<h2 style="{H2}">{feat['short']}</h2>
<p style="margin: 16px 0 0; {DISP}; font-size: 34px; color: {ROSE}">{feat['price']}</p>
<p style="{P}; margin-top: 18px; font-size: 18px; max-width: 520px">{FEATURE_WHY[feat['id']]}</p>
<div style="margin-top: 28px; display: flex; flex-wrap: wrap; gap: 14px"><a href="#book" style="{BTN}">Book {feat['nav']}</a><a href="{feat['slug']}.dc.html" style="{BTN_O}">Treatment details</a></div>
</div>
{ph(feat['ba'][0], feat['ba'][1], 'flex: 1 1 400px; min-width: 0; aspect-ratio: 4 / 3; border-radius: 4px')}
</section>
<section style="background: #F1E4E0"><div style="{WRAP}; padding-top: 96px; padding-bottom: 96px; display: flex; flex-wrap: wrap; gap: 40px 80px">
<div style="flex: 1 1 340px"><p style="{EYEBROW}">Full menu</p><h2 style="{H2}">More treatments for {a['name']} clients</h2><p style="{P}; margin-top: 20px">{a['p2']}</p></div>
<div style="flex: 2 1 560px; min-width: 0">{svc_rows}</div>
</div></section>
<section style="{WRAP}; padding-top: 96px; padding-bottom: 40px">
<figure style="margin: 0; max-width: 900px"><blockquote style="margin: 0; {DISP}; font-style: italic; font-size: clamp(28px, 3.2vw, 44px); line-height: 1.25">[Paste a review from a {a['name']} client]</blockquote><figcaption style="margin-top: 20px; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">[Client first name] · {a['name']}</figcaption></figure>
</section>
<section style="{WRAP}; padding-top: 64px; padding-bottom: 104px; display: flex; flex-wrap: wrap; gap: 48px 80px">
<div style="flex: 1 1 320px"><p style="{EYEBROW}">Questions</p><h2 style="{H2}">{a['name']} questions</h2></div>
<div style="flex: 2 1 560px; min-width: 0">{faq_list(faqs)}</div>
</section>
'''
    page += booking_block(feat['id'], f'Book from {a["name"]}', f'Choose what you are booking and pick a time.')
    page += f'''
<section style="{WRAP}; padding-top: 88px; padding-bottom: 104px">
<p style="{EYEBROW}">Other areas we serve</p>
<div style="display: flex; flex-wrap: wrap; gap: 10px">{other}</div>
</section>
'''
    page += footer()
    page += tail({"$preview": {"width": 1440, "height": 5200}}, SIMPLE_LOGIC)
    FILES[f"{a['slug']}.dc.html"] = page

# ---------- SERVICES HUB ----------
page = head('Injectable Treatments in San Antonio | Prices | Beautified Studios',
            'See every treatment at Beautified Studios in San Antonio: lip filler, lip flip, Daxxify, jaw filler, non-surgical nose job and facial balancing, with prices.')
page += nav()
page += crumbs([('Home', 'Main.dc.html'), ('Treatments', None)])
page += f'''
<section style="background: {INK}; color: {PAPER}"><div style="{WRAP}; padding-top: 72px; padding-bottom: 88px; display: flex; flex-wrap: wrap; gap: 48px 64px; align-items: flex-end">
<div style="flex: 2 1 600px; min-width: 0"><p style="{EYEBROW_D}">Treatments &amp; prices</p><h1 style="margin: 0; {DISP}; font-weight: 400; font-size: clamp(52px, 7vw, 112px); line-height: 1.04; letter-spacing: -0.01em">Injectable Treatments in <em style="color: #E7B9C1">San Antonio</em></h1></div>
<div style="flex: 1 1 340px; min-width: 0; display: grid; grid-template-columns: 1fr auto; gap: 12px 24px; font-size: 16px; border-top: 1px solid #3A2F31; padding-top: 20px">
<span>Lip Flip</span><span>$150</span><span>Jaw Filler</span><span>$1,449</span><span>Non-Surgical Nose Job</span><span>From $1,500</span><span>Full Facial Balancing</span><span>$1,954</span><span>Lip Filler · Daxxify</span><span>At consult</span>
</div></div></section>
<div style="height: 72px"></div>
<section style="{WRAP}; padding-bottom: 104px">{service_index()}</section>
<section style="background: {WINE}; color: {PAPER}">
<div style="{WRAP}; padding-top: 96px; padding-bottom: 96px; display: flex; flex-wrap: wrap; gap: 40px; align-items: center; justify-content: space-between">
<div style="flex: 1 1 520px"><p style="{EYEBROW_D}">Pay over time</p><p style="margin: 0; {DISP}; font-size: clamp(34px, 4vw, 56px); line-height: 1.05">Buy now, pay later from $50 to $4,000.</p><p style="margin: 16px 0 0; color: #E9D5D1">Get approved before your appointment and split your treatment into payments.</p></div>
<a href="{BOOK_URL}" style="{BTN_L}">Book a treatment</a>
</div>
</section>
'''
page += booking_block()
page += footer()
page += tail({"$preview": {"width": 1440, "height": 4400}}, SIMPLE_LOGIC)
FILES['services.dc.html'] = page

# ---------- AREAS HUB ----------
cards = ''.join(f'''<a href="{a['slug']}.dc.html" style="display: flex; flex-direction: column; gap: 14px; padding: 32px 0; border-top: 1px solid {INK}; text-decoration: none; color: {INK}"><span style="{DISP}; font-size: clamp(34px, 3.6vw, 52px); line-height: 1">{a['name']}</span><span style="font-size: 15px; color: {MUTED}">{a['p1'][:150].rsplit(' ', 1)[0]}…</span><span style="font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; color: {ROSE}">{a['name']} page →</span></a>''' for a in AREAS)
page = head('Areas We Serve | Cosmetic Injector San Antonio | Beautified Studios',
            'Beautified Studios serves clients from the Medical Center, Alamo Heights, Stone Oak, Leon Valley, Helotes, Boerne and all of San Antonio.')
page += nav()
page += crumbs([('Home', 'Main.dc.html'), ('Areas we serve', None)])
page += f'''
<section style="{WRAP}; padding-top: 48px; padding-bottom: 72px; display: flex; flex-wrap: wrap; gap: 32px 64px; align-items: flex-end">
<h1 style="flex: 2 1 640px; margin: 0; {DISP}; font-weight: 400; font-size: clamp(52px, 7vw, 112px); line-height: 1.04; letter-spacing: -0.01em">Areas We Serve in <em style="color: {ROSE}">San Antonio</em></h1>
<p style="{P}; flex: 1 1 340px; font-size: 19px">Our studio is at 1603 Babcock Rd, Suite 230. Clients book with us from across San Antonio and the Hill Country.</p>
</section>
<section style="{WRAP}; padding-bottom: 72px">{ph('MAP', 'Map of San Antonio with studio pin and service areas', 'width: 100%; min-height: 480px; border-radius: 4px; background: #E8DCD8')}</section>
<section style="{WRAP}; padding-bottom: 104px"><div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 0 48px">{cards}</div></section>
'''
page += visit_block()
page += footer()
page += tail({"$preview": {"width": 1440, "height": 3600}}, SIMPLE_LOGIC)
FILES['service-areas.dc.html'] = page

# ---------- FAQ PAGE ----------
groups = ''.join(f'''<div id="g{n}" style="display: flex; flex-wrap: wrap; gap: 24px 80px; padding-bottom: 80px"><h2 style="flex: 1 1 280px; margin: 0; {DISP}; font-weight: 400; font-size: 40px; line-height: 1.1">{g}</h2><div style="flex: 2 1 560px; min-width: 0">{faq_list(items)}</div></div>''' for n, (g, items) in enumerate(FAQ_GROUPS))
page = head('FAQ | Lip Filler, Daxxify &amp; Injectables in San Antonio | Beautified Studios',
            'Answers to common questions about lip filler, lip flips, Daxxify, non-surgical nose jobs, pricing, financing and booking at Beautified Studios in San Antonio.')
page += nav()
page += crumbs([('Home', 'Main.dc.html'), ('FAQ', None)])
page += f'''
<section style="background: #F1E4E0; margin-top: 28px"><div style="{WRAP}; padding-top: 88px; padding-bottom: 88px; text-align: center">
<p style="{EYEBROW}">{sum(len(i) for _, i in FAQ_GROUPS)} answers</p>
<h1 style="margin: 0; {DISP}; font-weight: 400; font-size: clamp(52px, 7vw, 112px); line-height: 1.04; letter-spacing: -0.01em">Injectables FAQ</h1>
<p style="{P}; margin: 24px auto 0; font-size: 19px; max-width: 560px">Lip filler, Daxxify, pricing, financing and booking at Beautified Studios in San Antonio. Still have a question? Call or text <a href="{TEL}" style="color: {INK}">{PHONE}</a>.</p>
<div style="margin-top: 32px; display: flex; flex-wrap: wrap; gap: 10px; justify-content: center">{''.join(f'<a href="#g{n}" style="background: #FFFFFF; border-radius: 999px; padding: 12px 22px; font-size: 15px; color: {INK}; text-decoration: none">{g}</a>' for n, (g, _) in enumerate(FAQ_GROUPS))}</div>
</div></section><div style="height: 88px"></div>
<section style="{WRAP}">{groups}</section>
'''
page += booking_block()
page += footer()
page += tail({"$preview": {"width": 1440, "height": 4800}}, SIMPLE_LOGIC)
FILES['faq.dc.html'] = page

# ---------- ABOUT ----------
page = head('About Brandy Gonzalez | Master Injector San Antonio | Beautified Studios',
            'Meet Brandy Gonzalez, owner of Beautified Studios and a Master Injector in San Antonio specializing in Daxxify and RHA filler. Injector training available.')
page += nav()
page += crumbs([('Home', 'Main.dc.html'), ('About', None)])
page += f'''
<section style="{WRAP}; padding-top: 48px; padding-bottom: 104px; display: flex; flex-wrap: wrap; gap: 56px; align-items: stretch">
<div style="flex: 1 1 560px; min-width: 0; display: flex; flex-direction: column; justify-content: space-between; gap: 40px">
<div><p style="{EYEBROW}">Owner &amp; Master Injector</p>
<h1 style="margin: 0; {DISP}; font-weight: 400; font-size: clamp(56px, 7.6vw, 124px); line-height: 1.02; letter-spacing: -0.01em">Brandy <em style="color: {ROSE}">Gonzalez</em></h1></div>
<div>
<p style="{P}; font-size: 19px; max-width: 540px">Brandy founded Beautified Studios with one promise: to fulfill any of your beautifying needs. With ten years in beauty and training through Monarch Master Injectors, she specializes in Daxxify and RHA filler.</p>
<p style="{P}; margin-top: 18px; max-width: 540px">Her approach is consultation first. Every client gets a plan built around their own proportions, so results look natural, balanced and unmistakably theirs.</p>
<p style="margin: 18px 0 0; font-size: 14px; color: {MUTED}">[ADD: licenses, certifications and years as an injector]</p>
</div>
</div>
{ph('P01', 'Brandy, editorial portrait', 'flex: 1 1 440px; min-width: 0; min-height: 680px; border-radius: 400px 400px 4px 4px')}
</section>
<section style="background: #F1E4E0">
<div style="{WRAP}; padding-top: 104px; padding-bottom: 104px; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px">
<div style="border-top: 1px solid {INK}; padding-top: 24px"><p style="margin: 0; {DISP}; font-style: italic; font-size: 20px; color: {ROSE}">01</p><h2 style="{H3}; margin-top: 10px">Consultation first</h2><p style="{P}; margin-top: 12px">You approve your plan and price before any treatment starts.</p></div>
<div style="border-top: 1px solid {INK}; padding-top: 24px"><p style="margin: 0; {DISP}; font-style: italic; font-size: 20px; color: {ROSE}">02</p><h2 style="{H3}; margin-top: 10px">Natural looking results</h2><p style="{P}; margin-top: 12px">RHA filler and Daxxify, chosen because results look natural when you talk and smile.</p></div>
<div style="border-top: 1px solid {INK}; padding-top: 24px"><p style="margin: 0; {DISP}; font-style: italic; font-size: 20px; color: {ROSE}">03</p><h2 style="{H3}; margin-top: 10px">Balanced proportions</h2><p style="{P}; margin-top: 12px">Lips, chin, jaw and cheeks are planned together so every feature fits your face.</p></div>
</div>
</section>
<section id="training" style="background: {WINE}; color: {PAPER}">
<div style="{WRAP}; padding-top: 120px; padding-bottom: 120px; display: flex; flex-wrap: wrap; gap: 56px; align-items: center">
{ph('P14', 'Brandy teaching a class', 'flex: 1 1 400px; min-width: 0; aspect-ratio: 4 / 3; border-radius: 4px')}
<div style="flex: 1 1 480px; min-width: 0">
<p style="{EYEBROW_D}">For beauty professionals</p>
<h2 style="{H2}; color: {PAPER}">Learn from a <em style="color: #F2D3D8">Master Injector</em></h2>
<p style="margin: 24px 0 0; color: #E9D5D1; max-width: 520px">Beautified Studios Academy offers 1:1 injector, permanent makeup and lash courses. Brandy also trains injectors through Monarch Master Injectors.</p>
<p style="margin: 14px 0 0; color: #D5BBB6; font-size: 14px">[ADD: course names, dates and pricing]</p>
<div style="margin-top: 32px; display: flex; flex-wrap: wrap; gap: 14px"><a href="academy.dc.html" style="{BTN_L}">See Academy courses</a><a href="mailto:{EMAIL}" style="display: inline-block; border: 1px solid {PAPER}; color: {PAPER}; text-decoration: none; padding: 17px 32px; border-radius: 999px; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase">Email Brandy</a></div>
</div>
</div>
</section>
'''
page += visit_block()
page += footer()
page += tail({"$preview": {"width": 1440, "height": 4300}}, SIMPLE_LOGIC)
FILES['about.dc.html'] = page

# ---------- BOOK PAGE ----------
page = head('Book Online | Beautified Studios San Antonio',
            'Book lip filler, Daxxify, jaw filler, facial balancing and more at Beautified Studios in San Antonio. Choose your time and pay online or in studio.')
page += nav()
page += f'''
<section style="{WRAP}; padding-top: 64px; padding-bottom: 104px">
<p style="{EYEBROW}">Online booking · San Antonio</p>
<h1 style="margin: 0 0 48px; {DISP}; font-weight: 400; font-size: clamp(52px, 7vw, 104px); line-height: 1.04; letter-spacing: -0.01em">Book your <em style="color: {ROSE}">appointment</em></h1>
<dc-import name="Scheduler" hint-size="100%,940px"></dc-import>
</section>
'''
page += footer()
page += tail({"$preview": {"width": 1440, "height": 2200}}, SIMPLE_LOGIC)
FILES['book.dc.html'] = page

# ---------- BLOG ----------
POSTS = [
    dict(slug='blog-lip-flip-vs-lip-filler', cat='Lips', date='November 2026', read='4 min read', photo=('P17', 'Lips close up, natural light'),
         title='Lip Flip vs. Lip Filler: Which Is Right for You?',
         seo='Lip Flip vs Lip Filler in San Antonio | Beautified Studios Blog',
         meta='Lip flip or lip filler? A San Antonio Master Injector explains the difference, cost, and who each treatment is best for.',
         dek='Two of the most requested lip treatments in San Antonio, and how to choose between them.',
         body=[
             ('p', 'If you have been scrolling lip transformations and wondering where to start, you are not alone. The two treatments clients ask about most at Beautified Studios are the lip flip and lip filler. They both change how your lips look, but they work in completely different ways.'),
             ('h', 'What a lip flip does'),
             ('p', 'A lip flip uses a small amount of wrinkle relaxer along the upper lip. It relaxes the muscle just enough for the lip to roll slightly outward, so more of it shows. Nothing is added, so the result is a subtle, natural looking pout. At Beautified Studios a lip flip is $150.'),
             ('h', 'What lip filler does'),
             ('p', 'Lip filler adds actual volume and shape. Brandy uses RHA filler, a hyaluronic acid filler designed to move with your expressions, so your lips look natural when you talk and smile. Filler can build fullness, define the lip border and improve symmetry.'),
             ('h', 'Which one should you choose?'),
             ('p', 'Choose a lip flip if you want a subtle change, are trying injectables for the first time, or show a lot of gum when you smile. Choose lip filler if you want noticeable volume or shape. Many clients start with a flip and move to filler later, and some do both.'),
             ('p', 'The easiest way to decide is a consultation. Brandy will look at your lips, listen to your goals and recommend what fits your face.'),
         ], cta=('lip-flip-san-antonio.dc.html', 'See the lip flip')),
    dict(slug='blog-what-is-daxxify', cat='Smoothing', date='November 2026', read='3 min read', photo=('P13', 'Daxxify product shot'),
         title='What Is Daxxify? A San Antonio Guide to the Longer Lasting Wrinkle Relaxer',
         seo='What Is Daxxify? San Antonio Guide | Beautified Studios Blog',
         meta='What is Daxxify and how is it different from Botox? A San Antonio Daxxify expert explains how it works and who it is for.',
         dek='How it compares to Botox, and why so many clients are making the switch.',
         body=[
             ('p', 'Daxxify is a wrinkle relaxing injectable in the same family as Botox. It softens expression lines, like the frown lines between your brows, by relaxing the muscles that cause them.'),
             ('h', 'How is it different from Botox?'),
             ('p', 'Both treatments work in a similar way. The big reason clients choose Daxxify is that it tends to last longer between appointments for many people, which means fewer visits to keep your results.'),
             ('h', 'Who is Daxxify for?'),
             ('p', 'Daxxify is a good fit if you want smoother expression lines and like the idea of spacing out your appointments. Brandy is a Daxxify specialist, so she can talk you through whether it is right for your goals.'),
             ('h', 'What to expect'),
             ('p', 'Your visit starts with a consultation. Treatment itself is a few quick injections, and lines soften gradually over the following couple of weeks. If anything needs adjusting, a Perfecting Session lets Brandy fine tune your results.'),
         ], cta=('daxxify-san-antonio.dc.html', 'See Daxxify')),
    dict(slug='blog-what-is-facial-balancing', cat='Contouring', date='November 2026', read='4 min read', photo=('P11', 'Facial balancing before / after'),
         title='What Is Facial Balancing, and Is It Right for You?',
         seo='What Is Facial Balancing? San Antonio | Beautified Studios Blog',
         meta='Facial balancing treats your whole face in proportion. Learn what is included, what it costs in San Antonio, and who it is best for.',
         dek='Why treating your face as a whole often looks more natural than treating one feature.',
         body=[
             ('p', 'Most people come in thinking about one feature, usually their lips. But often what makes a face look refreshed is how its features work together. That is the idea behind facial balancing.'),
             ('h', 'What facial balancing means'),
             ('p', 'Instead of treating one area in isolation, Brandy looks at your lips, chin, jawline and cheeks together. Small changes in the right places bring everything into proportion, so the result looks natural rather than done.'),
             ('h', 'What is included at Beautified Studios'),
             ('p', 'Full Facial Balancing is $1,954 and includes three syringes of filler placed where your face needs them most, plus a complimentary lip flip. The appointment takes about 90 minutes, including your consultation.'),
             ('h', 'Who it is best for'),
             ('p', 'It is ideal if you want an overall refresh, if you are not sure which single area to start with, or if you are traveling in from outside San Antonio and want to do more in one visit. Pay later financing is available in studio for treatments from $50 to $4,000.'),
         ], cta=('facial-balancing-san-antonio.dc.html', 'See facial balancing')),
]

def post_card(p_):
    return f'''<a href="{p_['slug']}.dc.html" style="display: flex; flex-direction: column; gap: 16px; text-decoration: none; color: {INK}">
{ph(p_['photo'][0], p_['photo'][1], 'width: 100%; aspect-ratio: 4 / 3; border-radius: 4px')}
<span style="font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {ROSE}">{p_['cat']} · {p_['read']}</span>
<span style="{DISP}; font-size: 30px; line-height: 1.15; letter-spacing: -0.01em">{p_['title']}</span>
<span style="font-size: 15px; color: {MUTED}">{p_['dek']}</span>
</a>'''

lead = POSTS[0]
page = head('Blog | Injectable Tips &amp; Guides from San Antonio | Beautified Studios',
            'Guides on lip filler, lip flips, Daxxify, facial balancing and more from Beautified Studios, a San Antonio cosmetic injector.')
page += nav()
page += crumbs([('Home', 'Main.dc.html'), ('Blog', None)])
page += f'''
<section style="{WRAP}; padding-top: 48px; padding-bottom: 72px; display: flex; flex-wrap: wrap; gap: 32px 64px; align-items: flex-end">
<h1 style="flex: 2 1 640px; margin: 0; {DISP}; font-weight: 400; font-size: clamp(52px, 7vw, 112px); line-height: 1.04; letter-spacing: -0.01em">Beautified Studios <em style="color: {ROSE}">Blog</em></h1>
<p style="{P}; flex: 1 1 340px; font-size: 19px">Guides to lip filler, Daxxify and other injectables from San Antonio Master Injector Brandy Gonzalez. New posts every week.</p>
</section>
<section style="{WRAP}; padding-bottom: 88px">
<a href="{lead['slug']}.dc.html" style="display: flex; flex-wrap: wrap; gap: 40px; align-items: center; text-decoration: none; color: {INK}; border-top: 1px solid {INK}; padding-top: 40px">
{ph(lead['photo'][0], lead['photo'][1], 'flex: 1 1 520px; min-width: 0; aspect-ratio: 16 / 10; border-radius: 4px')}
<span style="flex: 1 1 400px; min-width: 0; display: flex; flex-direction: column; gap: 18px">
<span style="font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {ROSE}">Featured · {lead['cat']} · {lead['read']}</span>
<span style="{DISP}; font-size: clamp(36px, 4vw, 56px); line-height: 1.05; letter-spacing: -0.01em">{lead['title']}</span>
<span style="font-size: 17px; color: {MUTED}">{lead['dek']}</span>
<span style="font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase">Read the post →</span>
</span>
</a>
</section>
<section style="{WRAP}; padding-bottom: 120px">
<p style="{EYEBROW}">Latest posts</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 48px 32px">{''.join(post_card(x) for x in POSTS[1:])}
<div style="display: flex; flex-direction: column; gap: 16px">
{ph('P18', 'Next weekly post photo', 'width: 100%; aspect-ratio: 4 / 3; border-radius: 4px')}
<span style="font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {ROSE}">Coming next week</span>
<span style="{DISP}; font-size: 30px; line-height: 1.15">[Weekly post title]</span>
</div>
</div>
</section>
'''
page += footer()
page += tail({"$preview": {"width": 1440, "height": 3400}}, SIMPLE_LOGIC)
FILES['blog.dc.html'] = page

for p_ in POSTS:
    body = ''
    for kind, txt in p_['body']:
        if kind == 'h':
            body += f'<h2 style="margin: 48px 0 0; {DISP}; font-weight: 400; font-size: 36px; line-height: 1.15; letter-spacing: -0.01em">{txt}</h2>'
        else:
            body += f'<p style="margin: 20px 0 0; font-size: 19px; line-height: 1.75; color: #3E3335">{txt}</p>'
    more = ''.join(post_card(x) for x in POSTS if x['slug'] != p_['slug'])
    page = head(p_['seo'], p_['meta'])
    page += nav()
    page += crumbs([('Home', 'Main.dc.html'), ('Blog', 'blog.dc.html'), (p_['cat'], None)])
    page += f'''
<article>
<header style="max-width: 900px; margin: 0 auto; padding: 56px 32px 48px; box-sizing: border-box">
<p style="{EYEBROW}">{p_['cat']} · {p_['date']} · {p_['read']}</p>
<h1 style="margin: 0; {DISP}; font-weight: 400; font-size: clamp(44px, 5.6vw, 80px); line-height: 1.0; letter-spacing: -0.01em">{p_['title']}</h1>
<p style="margin: 24px 0 0; {DISP}; font-style: italic; font-size: 24px; line-height: 1.35; color: {ROSE}">{p_['dek']}</p>
<p style="margin: 28px 0 0; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; color: {MUTED}">By Brandy Gonzalez, Master Injector</p>
</header>
<div style="{WRAP}">{ph(p_['photo'][0], p_['photo'][1], 'width: 100%; aspect-ratio: 21 / 9; border-radius: 4px')}</div>
<div style="max-width: 720px; margin: 0 auto; padding: 40px 32px 96px; box-sizing: border-box">
{body}
<div style="margin-top: 56px; background: #F1E4E0; padding: 36px; display: flex; flex-wrap: wrap; gap: 20px; justify-content: space-between; align-items: center">
<p style="margin: 0; {DISP}; font-size: 28px; line-height: 1.15; flex: 1 1 280px">Book your appointment in San Antonio.</p>
<div style="display: flex; flex-wrap: wrap; gap: 12px"><a href="{BOOK_URL}" style="{BTN}">Book now</a><a href="{p_['cta'][0]}" style="{BTN_O}">{p_['cta'][1]}</a></div>
</div>
</div>
</article>
<section style="background: #F1E4E0">
<div style="{WRAP}; padding-top: 96px; padding-bottom: 104px">
<p style="{EYEBROW}">Keep reading</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 48px 32px">{more}</div>
</div>
</section>
'''
    page += footer()
    page += tail({"$preview": {"width": 1440, "height": 3600}}, SIMPLE_LOGIC)
    FILES[f"{p_['slug']}.dc.html"] = page

# ---------- CONTACT ----------
lab = f'display: flex; flex-direction: column; gap: 8px; font-size: 12px; letter-spacing: 0.2em; text-transform: uppercase; color: {MUTED}'
inp = f'font-family: inherit; font-size: 16px; letter-spacing: 0; text-transform: none; padding: 16px; border: 1px solid {LINE}; border-radius: 4px; background: #FFFFFF; color: {INK}'
page = head('Contact | Beautified Studios | 1603 Babcock Rd, San Antonio',
            'Contact Beautified Studios in San Antonio. Call or text (726) 242-2952, email, or visit 1603 Babcock Rd, Suite 230.')
page += nav()
page += crumbs([('Home', 'Main.dc.html'), ('Contact', None)])
page += f'''
<section style="{WRAP}; padding-top: 48px; padding-bottom: 104px; display: flex; flex-wrap: wrap; gap: 64px">
<div style="flex: 1 1 440px; min-width: 0">
<h1 style="margin: 0; {DISP}; font-weight: 400; font-size: clamp(52px, 7vw, 112px); line-height: 1.04; letter-spacing: -0.01em">Contact Beautified Studios</h1>
<p style="{P}; margin-top: 24px; font-size: 19px; max-width: 460px">Questions about a treatment, pricing or training? Send a note and Brandy will get back to you. Ready to book? <a href="{BOOK_URL}" style="color: {INK}">Book online</a>.</p>
<div style="margin-top: 48px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 32px; border-top: 1px solid {LINE}; padding-top: 32px">
<div><p style="margin: 0; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">Call or text</p><p style="margin: 6px 0 0; {DISP}; font-size: 26px"><a href="{TEL}" style="color: {INK}; text-decoration: none">{PHONE}</a></p></div>
<div><p style="margin: 0; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">Email</p><p style="margin: 6px 0 0; font-size: 17px"><a href="mailto:{EMAIL}" style="color: {INK}">{EMAIL}</a></p></div>
<div><p style="margin: 0; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">Studio</p><p style="margin: 6px 0 0; font-size: 17px">{ADDR1}<br>{ADDR2}</p></div>
<div><p style="margin: 0; font-size: 13px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">Follow</p><p style="margin: 6px 0 0; font-size: 17px"><a href="{IG}" style="color: {INK}">Instagram</a> · <a href="{FB}" style="color: {INK}">Facebook</a></p></div>
</div>
</div>
<form aria-label="Contact form" style="flex: 1 1 480px; min-width: 0; background: #F1E4E0; padding: 48px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; align-content: start; box-sizing: border-box">
<label style="{lab}">Name<input type="text" autocomplete="name" style="{inp}"></label>
<label style="{lab}">Phone<input type="tel" autocomplete="tel" style="{inp}"></label>
<label style="{lab}; grid-column: 1 / -1">Email<input type="email" autocomplete="email" style="{inp}"></label>
<label style="{lab}; grid-column: 1 / -1">I am interested in<input type="text" placeholder="Lip filler, Daxxify, training…" style="{inp}"></label>
<label style="{lab}; grid-column: 1 / -1">Message<textarea rows="5" style="{inp}; resize: vertical"></textarea></label>
<button type="button" style="grid-column: 1 / -1; justify-self: start; background: {WINE}; color: {PAPER}; border: 0; padding: 18px 34px; border-radius: 999px; font-family: inherit; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer">Send message</button>
</form>
</section>
'''
page += visit_block()
page += footer()
page += tail({"$preview": {"width": 1440, "height": 3000}}, SIMPLE_LOGIC)
FILES['contact.dc.html'] = page



# ---------- ACADEMY ----------
COURSES = [
    ('1:1 Injector Training', 'Hands-on injectables training with Brandy, a Master Injector trained through Monarch Master Injectors.', '[Price]', '[Length]'),
    ('1:1 Permanent Makeup Course', 'The fundamentals and basics of starting your permanent makeup career, taught one on one.', '$599', '[Length]'),
    ('1:1 Lash Course', 'Private lash training with step by step instruction and hands-on practice.', '[Price]', '[Length]'),
]
crs = ''.join(f'''<div style="flex: 1 1 320px; min-width: 0; background: #FFFFFF; border: 1px solid {LINE}; border-radius: 4px; padding: 36px; display: flex; flex-direction: column; gap: 14px">
<p style="margin: 0; {DISP}; font-style: italic; font-size: 20px; color: {ROSE}">0{n+1}</p>
<h3 style="{H3}">{t}</h3><p style="{P}">{d}</p>
<div style="margin-top: auto; padding-top: 18px; border-top: 1px solid {LINE}; display: flex; justify-content: space-between; font-size: 16px"><span style="color: {MUTED}">{ln}</span><span style="font-weight: 500; color: {ROSE}">{p}</span></div>
<a href="contact.dc.html" style="{BTN}; text-align: center">Apply for this course</a>
</div>''' for n, (t, d, p, ln) in enumerate(COURSES))
page = head('Beautified Studios Academy | Injector, PMU &amp; Lash Training in San Antonio',
            'Beautified Studios Academy in San Antonio offers 1:1 injector training, permanent makeup courses and lash courses with Master Injector Brandy Gonzalez.')
page += nav()
page += crumbs([('Home', 'Main.dc.html'), ('Academy', None)])
page += f'''
<section style="{WRAP}; padding-top: 48px; padding-bottom: 96px; display: flex; flex-wrap: wrap; gap: 56px; align-items: stretch">
<div style="flex: 1 1 560px; min-width: 0; display: flex; flex-direction: column; justify-content: center">
<p style="{EYEBROW}">For beauty professionals</p>
<h1 style="margin: 0; {DISP}; font-weight: 400; font-size: clamp(52px, 7vw, 108px); line-height: 1.02; letter-spacing: -0.01em">Beautified Studios <em style="color: {ROSE}">Academy</em></h1>
<p style="{P}; margin-top: 24px; font-size: 20px; max-width: 560px">1:1 beauty training in San Antonio. Learn injectables, permanent makeup or lashes one on one with Brandy Gonzalez and leave with a certificate of completion.</p>
<div style="margin-top: 32px; display: flex; flex-wrap: wrap; gap: 14px"><a href="#courses" style="{BTN}">View courses</a><a href="{TEL}" style="{BTN_O}">Call {PHONE}</a></div>
</div>
{ph('P26', 'Academy graduate photo', 'flex: 1 1 420px; min-width: 0; min-height: 600px; border-radius: 400px 400px 4px 4px')}
</section>
<section style="background: {INK}; color: {PAPER}"><div style="{WRAP}; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr))">
<div style="padding: 32px 24px 32px 0"><p style="margin: 0; {DISP}; font-size: 28px">1:1 only</p><p style="margin: 6px 0 0; color: #D9C9C6">Private training, never a crowded class</p></div>
<div style="padding: 32px 24px; border-left: 1px solid #3A2F31"><p style="margin: 0; {DISP}; font-size: 28px">Hands-on</p><p style="margin: 6px 0 0; color: #D9C9C6">Practice with real technique</p></div>
<div style="padding: 32px 24px; border-left: 1px solid #3A2F31"><p style="margin: 0; {DISP}; font-size: 28px">Certificate</p><p style="margin: 6px 0 0; color: #D9C9C6">Certificate of completion</p></div>
<div style="padding: 32px 24px; border-left: 1px solid #3A2F31"><p style="margin: 0; {DISP}; font-size: 28px">10 years</p><p style="margin: 6px 0 0; color: #D9C9C6">Of beauty experience behind it</p></div>
</div></section>
<section id="courses" style="{WRAP}; padding-top: 104px; padding-bottom: 104px">
<p style="{EYEBROW}">Courses</p><h2 style="{H2}; margin-bottom: 48px">Choose your course</h2>
<div style="display: flex; flex-wrap: wrap; gap: 20px">{crs}</div>
<p style="{P}; margin-top: 24px">[Confirm course prices, length and what is included with Brandy.]</p>
</section>
<section style="background: #F1E4E0"><div style="{WRAP}; padding-top: 104px; padding-bottom: 104px; display: flex; flex-wrap: wrap; gap: 56px; align-items: center">
{ph('P27', 'Academy class in session', 'flex: 1 1 480px; min-width: 0; aspect-ratio: 4 / 3; border-radius: 4px')}
<div style="flex: 1 1 420px; min-width: 0"><p style="{EYEBROW}">How it works</p><h2 style="{H2}">From first class to certified</h2>
<div style="margin-top: 32px">{faq_list([('How do I sign up?', 'Apply through the contact form or call the studio. Brandy will confirm dates and send your enrollment details.'), ('Do I need experience?', '[Confirm requirements for each course.]'), ('Do I get a certificate?', 'Yes. Students receive a certificate of completion.')])}</div></div>
</div></section>
'''
page += footer()
page += tail({"$preview": {"width": 1440, "height": 3800}}, SIMPLE_LOGIC)
FILES['academy.dc.html'] = page

# ---------- PHOTO CHECKLIST ----------
rows = ''.join(f'''<tr><td style="padding: 18px 16px 18px 0; border-top: 1px solid {LINE}; vertical-align: top; font-weight: 600; color: {ROSE}; white-space: nowrap">{c}</td><td style="padding: 18px 16px; border-top: 1px solid {LINE}; vertical-align: top"><span style="{DISP}; font-size: 22px; display: block">{t}</span><span style="font-size: 15px; color: {MUTED}">{d}</span></td><td style="padding: 18px 16px; border-top: 1px solid {LINE}; vertical-align: top; font-size: 15px">{w}</td><td style="padding: 18px 0 18px 16px; border-top: 1px solid {LINE}; vertical-align: top; font-size: 15px; white-space: nowrap">{o}</td></tr>''' for c, t, d, w, o in PHOTOS)
other = [('Logo files', 'Any versions she has: the Beautified Studios logo and the Da Injector script logo, ideally as PNG or SVG.'),
         ('3 to 6 client reviews', 'Copied from Google, Instagram or texts, with a first name and the treatment.'),
         ('Licenses and certifications', 'What she is licensed as and her Monarch Master Injectors credentials, to list on the About page.'),
         ('Training details', 'Course names, dates, format and pricing for the Training section.'),
         ('Confirm lip flip price', 'GlossGenius lists $150, her promo says $200 value. Which one goes on the site?'),
         ('Confirm business name', 'Beautified Studios, Da Injector or Beautified Aesthetics: the one she wants to rank on Google.'),
         ('Confirm service areas', 'Which parts of San Antonio her clients actually come from, so the area pages match.'),
         ('Google Business Profile access', 'So we can match the site and profile and start building reviews.')]
other_html = ''.join(f'''<div style="display: flex; gap: 18px; padding: 20px 0; border-top: 1px solid {LINE}"><span aria-hidden="true" style="flex: 0 0 22px; height: 22px; border: 1.5px solid {ROSE}; border-radius: 4px; margin-top: 4px"></span><span><span style="{DISP}; font-size: 22px; display: block">{t}</span><span style="font-size: 15px; color: {MUTED}">{d}</span></span></div>''' for t, d in other)
page = head('What We Need | Beautified Studios Website', 'Photo and content checklist for the Beautified Studios website.')
page += f'''
<section style="background: {WINE}; color: {PAPER}"><div style="{WRAP}; padding-top: 72px; padding-bottom: 72px">
{wordmark(True)}
<h1 style="margin: 40px 0 0; {DISP}; font-weight: 400; font-size: clamp(48px, 6vw, 92px); line-height: 1.04">What we need from you</h1>
<p style="margin: 20px 0 0; font-size: 19px; color: #E9D5D1; max-width: 640px">Everything below fills the photo boxes and blanks across the new site. Phone photos are fine, the clearer and better lit the better. Every client photo needs the client\'s consent.</p>
</div></section>
<section style="{WRAP}; padding-top: 88px; padding-bottom: 40px">
<p style="{EYEBROW}">Photos · {len(PHOTOS)} shots</p>
<h2 style="{H2}; margin-bottom: 32px">Photo checklist</h2>
<div style="overflow-x: auto"><table style="width: 100%; min-width: 760px; border-collapse: collapse; font-size: 16px">
<thead><tr><th scope="col" style="text-align: left; padding: 0 16px 14px 0; font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">Code</th><th scope="col" style="text-align: left; padding: 0 16px 14px; font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">Photo</th><th scope="col" style="text-align: left; padding: 0 16px 14px; font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">Where it goes</th><th scope="col" style="text-align: left; padding: 0 0 14px 16px; font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">Shape</th></tr></thead>
<tbody>{rows}</tbody></table></div>
</section>
<section style="{WRAP}; padding-top: 72px; padding-bottom: 104px">
<p style="{EYEBROW}">Everything else</p>
<h2 style="{H2}; margin-bottom: 24px">Info &amp; decisions</h2>
<div style="max-width: 900px">{other_html}</div>
</section>
'''
page += tail({"$preview": {"width": 1440, "height": 3400}}, SIMPLE_LOGIC)
FILES['photo-checklist.dc.html'] = page

# ---------- write ----------
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, html in FILES.items():
        with open(os.path.join(OUT, name), 'w') as f:
            f.write(html)
    print(len(FILES), 'pages')
