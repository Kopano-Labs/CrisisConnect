// CrisisConnect Client Logic

document.addEventListener('DOMContentLoaded', () => {
    const dispatchTicker = document.getElementById('dispatch-ticker');
    const auditLog = document.getElementById('audit-log');
    const btnRefresh = document.getElementById('btn-refresh-dispatch');
    const latencyVal = document.getElementById('latency-val');

    const mockDispatches = [
        { node: 'CRISIS-C', msg: 'Coordination node sector_03 initialized.', ts: '01:20:00' },
        { node: 'FREDDY', msg: 'Pavement moisture level stable at 14.2%.', ts: '01:18:24' },
        { node: 'EDDIE', msg: 'BGF mining uptime alert: rock survey green.', ts: '01:15:10' },
        { node: 'KC-MAIN', msg: 'Lattice crossing verified. Seal generated.', ts: '01:10:45' },
        { node: 'ALTAR-3', msg: 'Classify-before-interpret pass complete.', ts: '01:05:00' }
    ];

    const mockAudits = [
        { time: '01:20:05', type: 'SEALED', note: 'sector_03_crisisconnect registered in Main Brain.' },
        { time: '01:19:12', type: 'SEALED', note: 'Lattice crossing swfus -> blackmask.' },
        { time: '01:14:22', type: 'PASS', note: 'PROOF-04 altar promotion pass.' },
        { time: '01:02:10', type: 'SEALED', note: 'Stateless renter entryway assert success.' }
    ];

    function populateDashboard() {
        // Populate dispatches
        dispatchTicker.innerHTML = '';
        mockDispatches.forEach(d => {
            const row = document.createElement('div');
            row.className = 'feed-row';
            row.innerHTML = `
                <span class="node-tag">${d.node}</span>
                <span class="node-msg">${d.msg}</span>
                <span class="node-ts">${d.ts}</span>
            `;
            dispatchTicker.appendChild(row);
        });

        // Populate audits
        auditLog.innerHTML = '';
        mockAudits.forEach(a => {
            const row = document.createElement('div');
            row.style.display = 'flex';
            row.style.justifyContent = 'space-between';
            row.style.padding = '8px 0';
            row.style.borderBottom = '1px solid rgba(255,255,255,0.03)';
            row.style.fontSize = '11px';
            row.innerHTML = `
                <span style="color: #10b981; font-weight: 600;">[${a.type}]</span>
                <span style="color: #9ca3af; margin-left: 10px; flex-grow: 1;">${a.note}</span>
                <span style="opacity: 0.6; font-family: monospace;">${a.time}</span>
            `;
            auditLog.appendChild(row);
        });
    }

    btnRefresh.addEventListener('click', () => {
        // Animate latency value
        latencyVal.style.color = '#00e5ff';
        const rand = (Math.random() * 2 + 3).toFixed(1);
        latencyVal.textContent = `${rand}ms`;
        
        // Add new log
        const now = new Date();
        const timeStr = now.toTimeString().split(' ')[0];
        mockDispatches.unshift({
            node: 'CRISIS-C',
            msg: `Self-audit executed. Verification pass: OK.`,
            ts: timeStr
        });
        if (mockDispatches.length > 6) mockDispatches.pop();
        
        populateDashboard();
        
        setTimeout(() => {
            latencyVal.style.color = '';
        }, 500);
    });

    populateDashboard();
});
