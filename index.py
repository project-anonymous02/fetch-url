<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nova Terminal Control</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #0a0e27;
            color: #00ff88;
            font-family: 'Courier New', monospace;
            overflow: hidden;
        }

        .container {
            display: flex;
            height: 100vh;
        }

        .sidebar {
            width: 250px;
            background: #0f1419;
            border-right: 2px solid #00ff88;
            padding: 20px;
            overflow-y: auto;
        }

        .sidebar h3 {
            color: #00ff88;
            margin-bottom: 15px;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .btn-group {
            margin-bottom: 20px;
        }

        .btn-group button {
            width: 100%;
            padding: 10px;
            margin-bottom: 8px;
            background: #1a2332;
            border: 1px solid #00ff88;
            color: #00ff88;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            transition: all 0.2s;
            text-align: left;
        }

        .btn-group button:hover {
            background: #00ff88;
            color: #0a0e27;
            transform: translateX(5px);
        }

        .btn-group button.active {
            background: #00ff88;
            color: #0a0e27;
        }

        .main {
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .header {
            background: #0f1419;
            border-bottom: 2px solid #00ff88;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .header h1 {
            font-size: 16px;
            color: #00ff88;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .status-indicator {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 12px;
        }

        .status-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #00ff88;
            animation: pulse 1s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        .content {
            flex: 1;
            display: flex;
            gap: 20px;
            padding: 20px;
            overflow: hidden;
        }

        .input-panel {
            width: 40%;
            background: #0f1419;
            border: 2px solid #00ff88;
            border-radius: 5px;
            padding: 15px;
            display: flex;
            flex-direction: column;
        }

        .input-panel h3 {
            color: #00ff88;
            margin-bottom: 10px;
            font-size: 13px;
            text-transform: uppercase;
        }

        .input-panel label {
            font-size: 11px;
            color: #00ff8833;
            margin-top: 10px;
            margin-bottom: 5px;
            display: block;
        }

        .input-panel select {
            background: #1a2332;
            border: 1px solid #00ff88;
            color: #00ff88;
            padding: 8px;
            margin-bottom: 10px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            cursor: pointer;
        }

        textarea {
            flex: 1;
            background: #1a2332;
            border: 1px solid #00ff88;
            color: #00ff88;
            padding: 10px;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            resize: none;
            margin-bottom: 10px;
        }

        textarea::placeholder {
            color: #00ff8844;
        }

        .control-buttons {
            display: flex;
            gap: 10px;
        }

        .control-buttons button {
            flex: 1;
            padding: 10px;
            background: #00ff88;
            border: none;
            color: #0a0e27;
            font-weight: bold;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            transition: all 0.2s;
            text-transform: uppercase;
        }

        .control-buttons button:hover {
            background: #00dd77;
            transform: scale(1.05);
        }

        .control-buttons button:active {
            transform: scale(0.98);
        }

        .control-buttons button.danger {
            background: #ff3333;
            color: white;
        }

        .control-buttons button.danger:hover {
            background: #ff5555;
        }

        .output-panel {
            flex: 1;
            background: #0f1419;
            border: 2px solid #00ff88;
            border-radius: 5px;
            padding: 15px;
            display: flex;
            flex-direction: column;
        }

        .output-panel h3 {
            color: #00ff88;
            margin-bottom: 10px;
            font-size: 13px;
            text-transform: uppercase;
        }

        #terminal {
            flex: 1;
            background: #0a0e27;
            border: 1px solid #00ff8844;
            padding: 10px;
            overflow-y: auto;
            font-size: 12px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
        }

        .output-line {
            margin-bottom: 2px;
        }

        .output-line.success {
            color: #00ff88;
        }

        .output-line.error {
            color: #ff3333;
        }

        .output-line.info {
            color: #88ccff;
        }

        .output-line.warning {
            color: #ffaa33;
        }

        .output-line.prompt {
            color: #00ff88;
        }

        .loading {
            color: #ffaa33;
            animation: blink 1s infinite;
        }

        @keyframes blink {
            0%, 49%, 100% { opacity: 1; }
            50%, 99% { opacity: 0.5; }
        }

        .clear-btn {
            padding: 8px 12px;
            background: #1a2332;
            border: 1px solid #00ff88;
            color: #00ff88;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-size: 11px;
            margin-top: 10px;
        }

        .clear-btn:hover {
            background: #00ff88;
            color: #0a0e27;
        }

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #0a0e27;
        }

        ::-webkit-scrollbar-thumb {
            background: #00ff88;
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #00dd77;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="sidebar">
            <h3>📋 Execution Type</h3>
            <div class="btn-group">
                <button class="mode-btn active" data-mode="api-python">🐍 API Python</button>
                <button class="mode-btn" data-mode="api-shell">🔧 API Shell</button>
                <button class="mode-btn" data-mode="loop-python">🔄 Loop Python</button>
                <button class="mode-btn" data-mode="loop-shell">🔄 Loop Shell</button>
                <button class="mode-btn" data-mode="fetch">🌐 Fetch URL</button>
                <button class="mode-btn" data-mode="context">📦 Shared Context</button>
                <button class="mode-btn" data-mode="search">🔍 Search</button>
            </div>

            <h3>⚙️ Settings</h3>
            <div class="btn-group">
                <label>Timeout (detik):</label>
                <input type="number" id="timeout" min="1" max="55" value="25" style="width: 100%; padding: 8px; background: #1a2332; border: 1px solid #00ff88; color: #00ff88; font-family: 'Courier New', monospace; margin-bottom: 10px;">
                
                <label>Base URL:</label>
                <input type="text" id="baseUrl" value="https://downloder-amber.vercel.app" style="width: 100%; padding: 8px; background: #1a2332; border: 1px solid #00ff88; color: #00ff88; font-family: 'Courier New', monospace; margin-bottom: 10px; font-size: 11px;">
            </div>

            <h3>🎯 Quick Actions</h3>
            <div class="btn-group">
                <button class="mode-btn" id="checkStatus">✅ Check Status</button>
                <button class="mode-btn" id="listLoops">📊 List Loops</button>
                <button class="mode-btn" id="getContext">📂 Get Context</button>
            </div>
        </div>

        <div class="main">
            <div class="header">
                <h1>🚀 NOVA TERMINAL CONTROL</h1>
                <div class="status-indicator">
                    <span class="status-dot"></span>
                    <span id="statusText">Ready</span>
                </div>
            </div>

            <div class="content">
                <div class="input-panel">
                    <h3>📝 Input Command</h3>
                    
                    <label id="modeLabel">Python Code:</label>
                    <textarea id="codeInput" placeholder="print('Hello Nova!')" spellcheck="false"></textarea>

                    <div id="loopOptions" style="display: none;">
                        <label>Wait Time (detik):</label>
                        <input type="number" id="waitTime" min="5" max="3600" value="60" style="width: 100%; padding: 8px; background: #1a2332; border: 1px solid #00ff88; color: #00ff88; font-family: 'Courier New', monospace; margin-bottom: 10px;">
                        
                        <label>Max Iterations:</label>
                        <input type="number" id="maxIterations" min="0" value="5" style="width: 100%; padding: 8px; background: #1a2332; border: 1px solid #00ff88; color: #00ff88; font-family: 'Courier New', monospace; margin-bottom: 10px;">
                    </div>

                    <div id="fetchOptions" style="display: none;">
                        <label>HTTP Method:</label>
                        <select id="fetchMethod" style="width: 100%; margin-bottom: 10px;">
                            <option>GET</option>
                            <option>POST</option>
                            <option>PUT</option>
                            <option>DELETE</option>
                        </select>

                        <label>Parse Mode:</label>
                        <select id="parseMode" style="width: 100%; margin-bottom: 10px;">
                            <option value="">None</option>
                            <option value="html">HTML</option>
                            <option value="json">JSON</option>
                            <option value="xml">XML</option>
                            <option value="auto">Auto</option>
                        </select>
                    </div>

                    <div id="contextOptions" style="display: none;">
                        <label>Action:</label>
                        <select id="contextAction" style="width: 100%; margin-bottom: 10px;">
                            <option value="get">View</option>
                            <option value="merge">Merge</option>
                            <option value="replace">Replace</option>
                            <option value="clear">Clear All</option>
                        </select>
                    </div>

                    <div class="control-buttons">
                        <button id="executeBtn">▶ EXECUTE</button>
                        <button id="stopBtn" class="danger" style="display: none;">⏹ STOP</button>
                    </div>
                </div>

                <div class="output-panel">
                    <h3>💻 Terminal Output</h3>
                    <div id="terminal"></div>
                    <button class="clear-btn" id="clearBtn">Clear Terminal</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        const BASE_URL = 'https://downloder-amber.vercel.app';
        const terminal = document.getElementById('terminal');
        const codeInput = document.getElementById('codeInput');
        const modeLabel = document.getElementById('modeLabel');
        const executeBtn = document.getElementById('executeBtn');
        const stopBtn = document.getElementById('stopBtn');
        const clearBtn = document.getElementById('clearBtn');
        const statusText = document.getElementById('statusText');
        const timeoutInput = document.getElementById('timeout');
        const baseUrlInput = document.getElementById('baseUrl');
        
        let currentMode = 'api-python';
        let isExecuting = false;

        // Mode buttons
        document.querySelectorAll('.mode-btn').forEach(btn => {
            if (!btn.id) {
                btn.addEventListener('click', function() {
                    document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    currentMode = this.dataset.mode;
                    updateUI();
                });
            }
        });

        function updateUI() {
            const loopOptions = document.getElementById('loopOptions');
            const fetchOptions = document.getElementById('fetchOptions');
            const contextOptions = document.getElementById('contextOptions');

            loopOptions.style.display = 'none';
            fetchOptions.style.display = 'none';
            contextOptions.style.display = 'none';

            switch(currentMode) {
                case 'api-python':
                    modeLabel.textContent = '🐍 Python Code:';
                    codeInput.placeholder = "print('Hello Nova!')";
                    break;
                case 'api-shell':
                    modeLabel.textContent = '🔧 Shell Command:';
                    codeInput.placeholder = "!ls -la";
                    break;
                case 'loop-python':
                    modeLabel.textContent = '🔄 Loop Python Code:';
                    codeInput.placeholder = "print('Loop iteration')";
                    loopOptions.style.display = 'block';
                    break;
                case 'loop-shell':
                    modeLabel.textContent = '🔄 Loop Shell Command:';
                    codeInput.placeholder = "!echo 'Running loop'";
                    loopOptions.style.display = 'block';
                    break;
                case 'fetch':
                    modeLabel.textContent = '🌐 URL to Fetch:';
                    codeInput.placeholder = "https://api.example.com/data";
                    fetchOptions.style.display = 'block';
                    break;
                case 'context':
                    modeLabel.textContent = '📦 Context Data (JSON):';
                    codeInput.placeholder = '{"key": "value"}';
                    contextOptions.style.display = 'block';
                    break;
                case 'search':
                    modeLabel.textContent = '🔍 Search Query:';
                    codeInput.placeholder = "python best practices";
                    break;
            }
        }

        function printOutput(text, type = 'info') {
            const line = document.createElement('div');
            line.className = `output-line ${type}`;
            line.textContent = text;
            terminal.appendChild(line);
            terminal.scrollTop = terminal.scrollHeight;
        }

        function printPrompt(text) {
            const line = document.createElement('div');
            line.className = 'output-line prompt';
            line.textContent = '▶ ' + text;
            terminal.appendChild(line);
            terminal.scrollTop = terminal.scrollHeight;
        }

        executeBtn.addEventListener('click', async () => {
            if (isExecuting) return;
            
            const code = codeInput.value.trim();
            if (!code) {
                printOutput('Error: Input tidak boleh kosong!', 'error');
                return;
            }

            isExecuting = true;
            executeBtn.style.display = 'none';
            stopBtn.style.display = 'block';
            statusText.textContent = 'Executing...';

            printPrompt(`${currentMode} > ${code.substring(0, 50)}${code.length > 50 ? '...' : ''}`);
            printOutput('...', 'loading');

            try {
                let url = baseUrlInput.value;
                let options = {
                    method: 'GET'
                };

                switch(currentMode) {
                    case 'api-python':
                    case 'api-shell':
                        url += `/api?code=${encodeURIComponent(code)}&timeout=${timeoutInput.value}`;
                        break;

                    case 'loop-python':
                    case 'loop-shell':
                        url += '/api/run/loop';
                        options.method = 'POST';
                        options.body = JSON.stringify({
                            code: code,
                            wait_time: parseInt(document.getElementById('waitTime').value),
                            max_iterations: parseInt(document.getElementById('maxIterations').value),
                            description: `Loop via terminal`
                        });
                        options.headers = { 'Content-Type': 'application/json' };
                        break;

                    case 'fetch':
                        url += '/api/fetch?url=' + encodeURIComponent(code) + '&parse=' + (document.getElementById('parseMode').value || '');
                        options.method = document.getElementById('fetchMethod').value;
                        break;

                    case 'context':
                        url += '/api/context';
                        const contextAction = document.getElementById('contextAction').value;
                        if (contextAction !== 'get') {
                            options.method = 'POST';
                            options.body = JSON.stringify({
                                action: contextAction,
                                data: contextAction === 'clear' ? {} : JSON.parse(code)
                            });
                            options.headers = { 'Content-Type': 'application/json' };
                        }
                        break;

                    case 'search':
                        url += `/api/search?summary=${encodeURIComponent(code)}`;
                        break;
                }

                terminal.removeChild(terminal.lastChild);

                const response = await fetch(url, options);
                const contentType = response.headers.get('content-type');
                
                let result;
                if (contentType?.includes('application/json')) {
                    result = await response.json();
                } else {
                    result = await response.text();
                }

                if (response.ok) {
                    printOutput('✓ Success', 'success');
                    
                    if (typeof result === 'object') {
                        printOutput(JSON.stringify(result, null, 2), 'success');
                    } else {
                        printOutput(result, 'success');
                    }

                    if (result.output) {
                        printOutput(result.output, 'info');
                    }
                    if (result.message) {
                        printOutput(result.message, 'info');
                    }
                } else {
                    printOutput('✗ Error: ' + response.status, 'error');
                    printOutput(typeof result === 'object' ? JSON.stringify(result, null, 2) : result, 'error');
                }
            } catch (error) {
                terminal.removeChild(terminal.lastChild);
                printOutput('✗ Error: ' + error.message, 'error');
            } finally {
                isExecuting = false;
                executeBtn.style.display = 'block';
                stopBtn.style.display = 'none';
                statusText.textContent = 'Ready';
            }
        });

        clearBtn.addEventListener('click', () => {
            terminal.innerHTML = '';
            printOutput('Terminal cleared', 'info');
        });

        // Quick actions
        document.getElementById('checkStatus').addEventListener('click', async () => {
            isExecuting = true;
            printPrompt('CHECK STATUS');
            printOutput('...', 'loading');
            
            try {
                const res = await fetch(baseUrlInput.value + '/');
                const data = await res.json();
                terminal.removeChild(terminal.lastChild);
                printOutput(JSON.stringify(data, null, 2), 'success');
            } catch (e) {
                terminal.removeChild(terminal.lastChild);
                printOutput('Error: ' + e.message, 'error');
            }
            isExecuting = false;
        });

        document.getElementById('listLoops').addEventListener('click', async () => {
            isExecuting = true;
            printPrompt('LIST LOOPS');
            printOutput('...', 'loading');
            
            try {
                const res = await fetch(baseUrlInput.value + '/api/run/loop?action=list');
                const data = await res.json();
                terminal.removeChild(terminal.lastChild);
                printOutput(JSON.stringify(data, null, 2), 'success');
            } catch (e) {
                terminal.removeChild(terminal.lastChild);
                printOutput('Error: ' + e.message, 'error');
            }
            isExecuting = false;
        });

        document.getElementById('getContext').addEventListener('click', async () => {
            isExecuting = true;
            printPrompt('GET CONTEXT');
            printOutput('...', 'loading');
            
            try {
                const res = await fetch(baseUrlInput.value + '/api/context');
                const data = await res.json();
                terminal.removeChild(terminal.lastChild);
                printOutput(JSON.stringify(data.context, null, 2), 'success');
            } catch (e) {
                terminal.removeChild(terminal.lastChild);
                printOutput('Error: ' + e.message, 'error');
            }
            isExecuting = false;
        });

        updateUI();
        printOutput('Nova Terminal Ready', 'success');
        printOutput('Select mode dan execute command', 'info');
    </script>
</body>
</html>
