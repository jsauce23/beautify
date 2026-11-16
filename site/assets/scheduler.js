/* Beautified Studios booking widget. Renders into any <div class="bs-scheduler" data-preset="id">. */
(function () {
  var GG = 'https://beautifedstudios.glossgenius.com/services';
  var SERVICES = [
    { id: 'flip', name: 'Lip Flip', price: '$150', dur: '60 min', note: 'Subtle, no filler' },
    { id: 'rha', name: 'Lip, Chin & Cheek Filler', price: 'At consult', dur: '60 min', note: 'RHA filler' },
    { id: 'dax', name: 'Daxxify', price: 'At consult', dur: '60 min', note: 'Softens fine lines' },
    { id: 'jaw', name: 'Jaw Filler', price: '$1,449', dur: '90 min', note: 'Sculpted jawline' },
    { id: 'nose', name: 'Non-Surgical Nose Job', price: 'From $1,500', dur: '90 min', note: 'Filler, no surgery' },
    { id: 'bal', name: 'Full Facial Balancing', price: '$1,954', dur: '90 min', note: '3 syringes + lip flip' },
    { id: 'perf', name: 'Perfecting Session', price: 'At consult', dur: '30 min', note: 'Botox or filler touch up' },
    { id: 'teeth', name: 'Teeth Whitening', price: '[Price]', dur: '[Time]', note: 'In-studio LED whitening' },
    { id: 'gem', name: 'Tooth Gem', price: '[Price]', dur: '[Time]', note: 'Add on to whitening' },
    { id: 'pmu', name: 'Brow Color Correction', price: '[Price]', dur: '[Time]', note: 'Fix brows gone bad' },
    { id: 'blush', name: 'Lip Blush', price: '$575', dur: '[Time]', note: 'Permanent lip color' },
    { id: 'secret', name: 'The Secret Service', price: 'Ask Brandy', dur: '90 min', note: 'If you know, you know' }
  ];
  var HOURS = { 2: [9, 17.5], 3: [9.5, 17], 4: [9.5, 17], 5: [9.5, 17], 6: [13.5, 16] };
  var DOWS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MONS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var SERIF = "font-family: 'DM Serif Display', Georgia, serif";
  var BTN = 'background: #4A1F28; color: #F7F0EC; border: 0; padding: 17px 34px; border-radius: 999px; font-family: inherit; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer';
  var BTN_O = 'background: transparent; color: #1A1314; border: 1px solid #1A1314; padding: 16px 30px; border-radius: 999px; font-family: inherit; font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer';
  var OPT = 'width: 100%; display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 18px 22px; border-radius: 4px; font-family: inherit; cursor: pointer; text-align: left; ';
  var ON = 'background: #F7F0EC; border: 1px solid #4A1F28; box-shadow: inset 4px 0 0 #8E4B57; ';
  var OFF = 'background: #FFFFFF; border: 1px solid #DCC6C1; ';
  var INP = 'font-family: inherit; font-size: 16px; padding: 15px; border: 1px solid #DCC6C1; border-radius: 4px; background: #F7F0EC; color: #1A1314';
  var LAB = 'display: flex; flex-direction: column; gap: 8px; font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; color: #463A3C';

  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fmt(h) { var hr = Math.floor(h), m = h % 1 ? '30' : '00'; return (hr > 12 ? hr - 12 : hr) + ':' + m + ' ' + (hr >= 12 ? 'PM' : 'AM'); }
  function days() {
    var out = [], b = new Date();
    for (var i = 1; i <= 15; i++) {
      var d = new Date(b.getFullYear(), b.getMonth(), b.getDate() + i), w = d.getDay();
      if (!HOURS[w]) continue;
      out.push({ key: d.toISOString().slice(0, 10), w: w, dow: DOWS[w], dnum: d.getDate(), mon: MONS[d.getMonth()], full: DOWS[w] + ', ' + MONS[d.getMonth()] + ' ' + d.getDate() });
    }
    return out;
  }

  function mount(root) {
    var st = { step: 1, svc: root.getAttribute('data-preset') || null, day: null, time: null, name: '', phone: '', email: '', notes: '', sending: false, error: '' };
    var DAYS = days();
    function svc() { return SERVICES.filter(function (s) { return s.id === st.svc; })[0] || null; }
    function day() { return DAYS.filter(function (d) { return d.key === st.day; })[0] || null; }
    function set(p) { for (var k in p) st[k] = p[k]; render(); }

    function steps() {
      return ['Treatment', 'Date &amp; time', 'Details', 'Confirm'].map(function (l, i) {
        var n = i + 1, c = st.step === n ? 'color: #4A1F28; font-weight: 600' : (st.step > n ? 'color: #8E4B57' : 'color: #463A3C');
        return '<li style="font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; ' + c + '"><span style="' + SERIF + '; font-style: italic; margin-right: 8px">0' + n + '</span>' + l + '</li>';
      }).join('');
    }
    function nav(back, next, label, disabled) {
      return '<div style="margin-top: 30px; display: flex; justify-content: ' + (back ? 'space-between' : 'flex-end') + '; gap: 12px; flex-wrap: wrap">' +
        (back ? '<button type="button" data-go="' + back + '" style="' + BTN_O + '">Back</button>' : '') +
        '<button type="button" data-go="' + next + '" ' + (disabled ? 'disabled style="' + BTN + '; opacity: .4; cursor: not-allowed"' : 'style="' + BTN + '"') + '>' + label + '</button></div>';
    }
    function h3(t, sub) { return '<h3 style="margin: 0 0 6px; ' + SERIF + '; font-weight: 400; font-size: 34px">' + t + '</h3><p style="margin: 0 0 24px; color: #463A3C">' + sub + '</p>'; }

    function body() {
      var s = svc(), d = day();
      if (st.step === 1) {
        return h3('Choose a treatment', 'Not sure? Pick the closest one. Brandy finalizes your plan at your visit.') +
          '<div style="display: flex; flex-direction: column; gap: 10px">' + SERVICES.map(function (x) {
            return '<button type="button" data-svc="' + x.id + '" style="' + OPT + (st.svc === x.id ? ON : OFF) + '"><span style="display: flex; flex-direction: column; gap: 2px"><span style="' + SERIF + '; font-size: 22px; color: #1A1314">' + esc(x.name) + '</span><span style="font-size: 14px; color: #463A3C">' + esc(x.dur) + ' · ' + esc(x.note) + '</span></span><span style="font-size: 15px; font-weight: 500; color: #8E4B57; white-space: nowrap">' + esc(x.price) + '</span></button>';
          }).join('') + '</div>' + nav(null, 2, 'Choose a time', !s);
      }
      if (st.step === 2) {
        var times = [];
        if (d) { var r = HOURS[d.w]; for (var h = r[0]; h <= r[1]; h += 1) times.push(fmt(h)); }
        return h3('Pick a date and time', 'Choose your preferred time. Brandy confirms every request.') +
          '<div style="display: flex; gap: 10px; overflow-x: auto; padding-bottom: 8px">' + DAYS.map(function (x) {
            var on = st.day === x.key;
            return '<button type="button" data-day="' + x.key + '" style="flex: 0 0 auto; width: 76px; display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 14px 0; border-radius: 4px; font-family: inherit; cursor: pointer; ' + (on ? 'background: #4A1F28; color: #F7F0EC; border: 1px solid #4A1F28' : 'background: #FFFFFF; color: #1A1314; border: 1px solid #DCC6C1') + '"><span style="font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase">' + x.dow + '</span><span style="' + SERIF + '; font-size: 30px; line-height: 1.1">' + x.dnum + '</span><span style="font-size: 12px">' + x.mon + '</span></button>';
          }).join('') + '</div>' +
          (d ? '<p style="margin: 28px 0 12px; font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; color: #463A3C">Open times · ' + d.full + '</p><div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 10px">' + times.map(function (t) {
            var on = st.time === t;
            return '<button type="button" data-time="' + t + '" style="min-height: 48px; padding: 12px; border-radius: 4px; font-family: inherit; font-size: 15px; cursor: pointer; ' + (on ? 'background: #8E4B57; color: #FFFFFF; border: 1px solid #8E4B57' : 'background: #FFFFFF; color: #1A1314; border: 1px solid #DCC6C1') + '">' + t + '</button>';
          }).join('') + '</div>' : '') + nav(1, 3, 'Your details', !st.time);
      }
      if (st.step === 3) {
        var ok = st.name.trim() && st.phone.trim() && st.email.trim();
        return h3('Your details', 'Your confirmation comes by text and email.') +
          '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 18px">' +
          '<label style="' + LAB + '">Full name<input data-f="name" type="text" autocomplete="name" value="' + esc(st.name) + '" style="' + INP + '"></label>' +
          '<label style="' + LAB + '">Mobile phone<input data-f="phone" type="tel" autocomplete="tel" value="' + esc(st.phone) + '" style="' + INP + '"></label>' +
          '<label style="' + LAB + '; grid-column: 1 / -1">Email<input data-f="email" type="email" autocomplete="email" value="' + esc(st.email) + '" style="' + INP + '"></label>' +
          '<label style="' + LAB + '; grid-column: 1 / -1">Anything Brandy should know? (optional)<input data-f="notes" type="text" value="' + esc(st.notes) + '" placeholder="First visit, goals, inspiration photos" style="' + INP + '"></label>' +
          '</div>' + nav(2, 4, 'Review', !ok);
      }
      if (st.step === 4) {
        return h3('Confirm your request', 'Brandy will text you to confirm your appointment. Payment and financing are handled at confirmation.') +
          '<div style="border: 1px solid #DCC6C1; border-radius: 4px; padding: 24px; display: grid; gap: 10px; font-size: 16px">' +
          '<div><strong>' + esc(s.name) + '</strong> · ' + esc(s.price) + '</div><div>' + d.full + ' at ' + st.time + '</div><div>' + esc(st.name) + ' · ' + esc(st.phone) + ' · ' + esc(st.email) + '</div></div>' +
          '<p style="margin: 20px 0 0; font-size: 15px; color: #463A3C">By booking you agree to our cancellation policy: at least 24 hours notice, or 50% of the service is charged.</p>' +
          (st.error ? '<p role="alert" style="margin: 16px 0 0; color: #8E4B57">' + esc(st.error) + '</p>' : '') +
          '<div style="margin-top: 28px; display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap"><button type="button" data-go="3" style="' + BTN_O + '">Back</button>' +
          '<div style="display: flex; gap: 12px; flex-wrap: wrap"><a href="' + GG + '" target="_blank" rel="noopener" style="' + BTN_O + '; text-decoration: none">Book &amp; pay on GlossGenius</a>' +
          '<button type="button" data-submit="1" ' + (st.sending ? 'disabled ' : '') + 'style="' + BTN + '">' + (st.sending ? 'Sending…' : 'Request appointment') + '</button></div></div>';
      }
      return '<div style="text-align: center; padding: 32px 0"><svg aria-hidden="true" width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="#8E4B57" stroke-width="1.5"><circle cx="32" cy="32" r="30"></circle><path d="M20 33l8 8 16-18"></path></svg>' +
        '<h3 style="margin: 20px 0 8px; ' + SERIF + '; font-weight: 400; font-size: 44px">Request sent, <em style="color: #8E4B57">' + esc(st.name.trim().split(' ')[0] || 'gorgeous') + '</em></h3>' +
        '<p style="margin: 0 auto; max-width: 460px; color: #463A3C">Brandy will text ' + esc(st.phone) + ' to confirm your ' + esc(s.name) + ' on ' + d.full + ' at ' + st.time + '.</p>' +
        '<div style="margin-top: 28px"><button type="button" data-reset="1" style="' + BTN_O + '">Book another</button></div></div>';
    }

    function summary() {
      var s = svc(), d = day();
      var row = function (l, v) { return '<div><p style="margin: 0; font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: #D5BBB6">' + l + '</p>' + v + '</div>'; };
      return '<p style="margin: 0 0 24px; font-size: 13px; letter-spacing: 0.14em; text-transform: uppercase; color: #E7B9C1">Your appointment</p><div style="display: flex; flex-direction: column; gap: 20px">' +
        row('Treatment', '<p style="margin: 4px 0 0; ' + SERIF + '; font-size: 26px; line-height: 1.15; color: #FFFFFF">' + (s ? esc(s.name) : 'Choose a treatment') + '</p><p style="margin: 2px 0 0; font-size: 14px; color: #E9D5D1">' + (s ? esc(s.dur) : '') + '</p>') +
        row('When', '<p style="margin: 4px 0 0; color: #FFFFFF">' + (d ? d.full + (st.time ? ' at ' + st.time : '') : 'Pick a date') + '</p>') +
        row('Where', '<p style="margin: 4px 0 0; color: #FFFFFF">1603 Babcock Rd, Suite 230<br>San Antonio, TX 78229</p>') +
        '<div style="border-top: 1px solid #6A3843; padding-top: 20px; display: flex; justify-content: space-between; align-items: baseline; gap: 12px"><span style="font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: #D5BBB6">Price</span><span style="' + SERIF + '; font-size: 28px; color: #FFFFFF">' + (s ? esc(s.price) : '—') + '</span></div></div>' +
        '<div style="margin-top: 24px; border: 1px solid #6A3843; border-radius: 4px; padding: 18px"><p style="margin: 0; font-size: 15px; color: #FFFFFF; font-weight: 500">Buy now, pay later</p><p style="margin: 4px 0 0; font-size: 14px; color: #E9D5D1">Split treatments from $50 to $4,000 into payments.</p></div>';
    }

    function render() {
      root.innerHTML = '<div style="display: flex; flex-wrap: wrap; gap: 24px; align-items: flex-start">' +
        '<div style="flex: 999 1 560px; min-width: 0; background: #FFFFFF; border: 1px solid #DCC6C1; border-radius: 4px; padding: clamp(22px, 4vw, 40px); box-sizing: border-box">' +
        '<ol aria-label="Booking steps" style="list-style: none; margin: 0 0 32px; padding: 0 0 20px; display: flex; flex-wrap: wrap; gap: 8px 28px; border-bottom: 1px solid #DCC6C1">' + steps() + '</ol>' + body() + '</div>' +
        '<aside aria-label="Booking summary" style="flex: 1 1 300px; min-width: 0; background: #4A1F28; color: #F7F0EC; border-radius: 4px; padding: 36px; box-sizing: border-box">' + summary() + '</aside></div>';
    }

    root.addEventListener('click', function (e) {
      var t = e.target.closest('button'); if (!t || t.disabled) return;
      if (t.dataset.svc) set({ svc: t.dataset.svc });
      else if (t.dataset.day) set({ day: t.dataset.day, time: null });
      else if (t.dataset.time) set({ time: t.dataset.time });
      else if (t.dataset.go) set({ step: +t.dataset.go, error: '' });
      else if (t.dataset.reset) set({ step: 1, svc: null, day: null, time: null });
      else if (t.dataset.submit) submit();
    });
    root.addEventListener('input', function (e) {
      var f = e.target.dataset && e.target.dataset.f; if (!f) return;
      st[f] = e.target.value;
      if (f !== 'notes') {
        var ok = st.name.trim() && st.phone.trim() && st.email.trim();
        var btn = root.querySelector('[data-go="4"]');
        if (btn) { btn.disabled = !ok; btn.style.opacity = ok ? '1' : '.4'; btn.style.cursor = ok ? 'pointer' : 'not-allowed'; }
      }
    });

    function submit() {
      var s = svc(), d = day();
      var data = { 'form-name': 'booking', treatment: s.name, date: d.full, time: st.time, name: st.name, phone: st.phone, email: st.email, notes: st.notes, page: location.pathname };
      set({ sending: true, error: '' });
      fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(data).toString() })
        .then(function (r) { if (!r.ok) throw new Error(); set({ sending: false, step: 5 }); })
        .catch(function () { set({ sending: false, error: 'Something went wrong. Please call or text (726) 242-2952, or book on GlossGenius.' }); });
    }
    render();
  }

  document.querySelectorAll('.bs-scheduler').forEach(mount);
})();
