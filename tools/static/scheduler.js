/* Beautified Studios booking form. Renders into any <div class="bs-scheduler" data-preset="id">. */
(function () {
  var GG = 'https://beautifedstudios.glossgenius.com/services';
  var SERVICES = [
    { id: 'flip', name: 'Lip Flip', price: '$150' },
    { id: 'rha', name: 'Lip, Chin or Cheek Filler', price: 'Priced at consult' },
    { id: 'dax', name: 'Daxxify', price: 'Priced at consult' },
    { id: 'jaw', name: 'Jaw Filler', price: '$1,449' },
    { id: 'nose', name: 'Non-Surgical Nose Job', price: 'From $1,500' },
    { id: 'bal', name: 'Full Facial Balancing', price: '$1,954' },
    { id: 'perf', name: 'Perfecting Session', price: 'Priced at consult' },
    { id: 'teeth', name: 'Teeth Whitening', price: '' },
    { id: 'gem', name: 'Tooth Gem', price: '' },
    { id: 'pmu', name: 'Brow Color Correction', price: '' },
    { id: 'blush', name: 'Lip Blush', price: '$575' },
    { id: 'consult', name: 'Not sure yet, I want a consultation', price: '' }
  ];
  var HOURS = { 2: [9, 17.5], 3: [9.5, 17], 4: [9.5, 17], 5: [9.5, 17], 6: [13.5, 16] };
  var DOWS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  var MONS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var SERIF = "font-family: 'DM Serif Display', Georgia, serif";
  var LABEL = 'display: block; margin: 0 0 12px; ' + SERIF + '; font-size: 24px; color: #1A1314';
  var INP = 'width: 100%; box-sizing: border-box; font-family: inherit; font-size: 17px; padding: 16px; border: 1px solid #DCC6C1; border-radius: 4px; background: #FFFFFF; color: #1A1314';
  var SMALL = 'display: flex; flex-direction: column; gap: 6px; font-size: 15px; color: #463A3C';

  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fmt(h) { var hr = Math.floor(h), m = h % 1 ? '30' : '00'; return (hr > 12 ? hr - 12 : hr) + ':' + m + ' ' + (hr >= 12 ? 'PM' : 'AM'); }
  function days() {
    var out = [], b = new Date();
    for (var i = 1; i <= 15; i++) {
      var d = new Date(b.getFullYear(), b.getMonth(), b.getDate() + i), w = d.getDay();
      if (!HOURS[w]) continue;
      out.push({ key: d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(), w: w, dow: DOWS[w], dnum: d.getDate(), mon: MONS[d.getMonth()], full: DOWS[w] + ', ' + MONS[d.getMonth()] + ' ' + d.getDate() });
    }
    return out;
  }

  function mount(root) {
    var DAYS = days();
    var st = { svc: root.getAttribute('data-preset') || '', day: null, time: null, name: '', phone: '', email: '', sending: false, done: false, error: '' };
    function svc() { return SERVICES.filter(function (s) { return s.id === st.svc; })[0] || null; }
    function day() { return DAYS.filter(function (d) { return d.key === st.day; })[0] || null; }
    function ready() { return svc() && st.day && st.time && st.name.trim() && st.phone.trim() && st.email.trim(); }

    function render() {
      var s = svc(), d = day();
      if (st.done) {
        root.innerHTML = '<div style="background: #FFFFFF; border: 1px solid #DCC6C1; border-radius: 4px; padding: 48px 24px; text-align: center">' +
          '<svg aria-hidden="true" width="56" height="56" viewBox="0 0 64 64" fill="none" stroke="#8E4B57" stroke-width="1.5"><circle cx="32" cy="32" r="30"></circle><path d="M20 33l8 8 16-18"></path></svg>' +
          '<h3 style="margin: 16px 0 8px; ' + SERIF + '; font-weight: 400; font-size: 38px">You\'re all set, ' + esc(st.name.trim().split(' ')[0]) + '</h3>' +
          '<p style="margin: 0 auto; max-width: 440px; color: #463A3C">Brandy will text ' + esc(st.phone) + ' to confirm your ' + esc(s.name) + ' on ' + d.full + ' at ' + st.time + '.</p></div>';
        return;
      }
      var opts = '<option value="">Choose a treatment</option>' + SERVICES.map(function (x) {
        return '<option value="' + x.id + '"' + (st.svc === x.id ? ' selected' : '') + '>' + esc(x.name) + (x.price ? ' · ' + esc(x.price) : '') + '</option>';
      }).join('');
      var dayBtns = DAYS.map(function (x) {
        var on = st.day === x.key;
        return '<button type="button" data-day="' + x.key + '" aria-pressed="' + on + '" style="flex: 0 0 auto; width: 72px; display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 12px 0; border-radius: 4px; font-family: inherit; cursor: pointer; ' + (on ? 'background: #4A1F28; color: #F7F0EC; border: 1px solid #4A1F28' : 'background: #FFFFFF; color: #1A1314; border: 1px solid #DCC6C1') + '"><span style="font-size: 13px">' + x.dow + '</span><span style="' + SERIF + '; font-size: 26px; line-height: 1.1">' + x.dnum + '</span><span style="font-size: 13px">' + x.mon + '</span></button>';
      }).join('');
      var times = '';
      if (d) {
        var r = HOURS[d.w], list = [];
        for (var h = r[0]; h <= r[1]; h += 1) list.push(fmt(h));
        times = '<div style="margin-top: 16px; display: grid; grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); gap: 10px">' + list.map(function (t) {
          var on = st.time === t;
          return '<button type="button" data-time="' + t + '" aria-pressed="' + on + '" style="min-height: 50px; border-radius: 4px; font-family: inherit; font-size: 16px; cursor: pointer; ' + (on ? 'background: #8E4B57; color: #FFFFFF; border: 1px solid #8E4B57' : 'background: #FFFFFF; color: #1A1314; border: 1px solid #DCC6C1') + '">' + t + '</button>';
        }).join('') + '</div>';
      }
      var ok = ready();
      root.innerHTML = '<form novalidate style="background: #FFFFFF; border: 1px solid #DCC6C1; border-radius: 4px; padding: clamp(24px, 4vw, 44px); display: flex; flex-direction: column; gap: 36px; max-width: 760px">' +
        '<div><label for="bs-svc" style="' + LABEL + '">What are you booking?</label><select id="bs-svc" data-f="svc" style="' + INP + '; appearance: auto">' + opts + '</select></div>' +
        '<div><p style="' + LABEL + '">Pick a day and time</p><div style="display: flex; gap: 10px; overflow-x: auto; padding-bottom: 6px">' + dayBtns + '</div>' + times + '</div>' +
        '<div><p style="' + LABEL + '">Your info</p><div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px">' +
        '<label style="' + SMALL + '">Name<input data-f="name" type="text" autocomplete="name" value="' + esc(st.name) + '" style="' + INP + '"></label>' +
        '<label style="' + SMALL + '">Phone<input data-f="phone" type="tel" autocomplete="tel" value="' + esc(st.phone) + '" style="' + INP + '"></label>' +
        '<label style="' + SMALL + '; grid-column: 1 / -1">Email<input data-f="email" type="email" autocomplete="email" value="' + esc(st.email) + '" style="' + INP + '"></label></div></div>' +
        '<div>' + (st.error ? '<p role="alert" style="margin: 0 0 14px; color: #8E4B57">' + esc(st.error) + '</p>' : '') +
        '<button type="submit" data-book="1" ' + (ok && !st.sending ? '' : 'disabled ') + 'style="width: 100%; background: #4A1F28; color: #F7F0EC; border: 0; padding: 20px; border-radius: 999px; font-family: inherit; font-size: 16px; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer; opacity: ' + (ok ? '1' : '.4') + '">' + (st.sending ? 'Booking…' : 'Book appointment') + '</button>' +
        '<p style="margin: 14px 0 0; font-size: 14px; color: #463A3C; text-align: center">Brandy confirms by text. 24 hour cancellation policy. Prefer to pay now? <a href="' + GG + '" target="_blank" rel="noopener" style="color: #8E4B57">Book on GlossGenius</a></p></div>' +
        '</form>';
    }

    function refreshButton() {
      var b = root.querySelector('[data-book]'); if (!b) return;
      var ok = ready(); b.disabled = !ok || st.sending; b.style.opacity = ok ? '1' : '.4';
    }

    root.addEventListener('click', function (e) {
      var t = e.target.closest('button'); if (!t || t.type === 'submit') return;
      if (t.dataset.day) { st.day = t.dataset.day; st.time = null; render(); }
      else if (t.dataset.time) { st.time = t.dataset.time; render(); }
    });
    root.addEventListener('change', function (e) {
      if (e.target.dataset && e.target.dataset.f === 'svc') { st.svc = e.target.value; refreshButton(); }
    });
    root.addEventListener('input', function (e) {
      var f = e.target.dataset && e.target.dataset.f;
      if (f && f !== 'svc') { st[f] = e.target.value; refreshButton(); }
    });
    root.addEventListener('submit', function (e) {
      e.preventDefault(); if (!ready() || st.sending) return;
      var s = svc(), d = day();
      st.sending = true; st.error = ''; render();
      var data = { 'form-name': 'booking', treatment: s.name, date: d.full, time: st.time, name: st.name, phone: st.phone, email: st.email, notes: '', page: location.pathname };
      fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(data).toString() })
        .then(function (r) { if (!r.ok) throw new Error(); st.sending = false; st.done = true; render(); })
        .catch(function () { st.sending = false; st.error = 'Something went wrong. Please call or text (726) 242-2952.'; render(); });
    });
    render();
  }

  document.querySelectorAll('.bs-scheduler').forEach(mount);
})();
