const vscode = require('vscode');
const { exec } = require('child_process');

function activate(context) {
    let disposable = vscode.commands.registerCommand('telegram-favorite-code.sendCode', function () {
        const editor = vscode.window.activeTextEditor;
        
        if (!editor) {
            vscode.window.showErrorMessage('No active editor found!');
            return;
        }

        const selection = editor.selection;
        let text = '';

        if (selection && !selection.isEmpty) {
            const selectionRange = new vscode.Range(selection.start, selection.end);
            text = editor.document.getText(selectionRange);
        } else {
            vscode.env.clipboard.readText().then(clipboardText => {
                if (clipboardText) {
                    text = clipboardText;
                    sendToTelegramDesktop(text);
                } else {
                    vscode.window.showErrorMessage('No text selected or in clipboard!');
                }
            });
            return;
        }

        if (text) {
            sendToTelegramDesktop(text);
        } else {
            vscode.window.showErrorMessage('No text to send!');
        }
    });

    context.subscriptions.push(disposable);
}

function sendToTelegramDesktop(text) {
    const maxLength = 4000;
    
    text = '```\n' + text + '\n```';
    
    if (text.length > maxLength) {
        const originalMaxLength = maxLength - 8;
        const trimmedText = text.substring(0, originalMaxLength) + '\n\n... (текст обрезан)';
        text = '```\n' + trimmedText + '\n```';
    }

    const encodedText = encodeURIComponent(text);
    const telegramUrl = `tg://msg?text=${encodedText}`;
    
    const platform = process.platform;
    let command;
    
    if (platform === 'win32') {
        command = `start "" "${telegramUrl}"`;
    } else if (platform === 'darwin') {
        command = `open "${telegramUrl}"`;
    } else {
        command = `xdg-open "${telegramUrl}" || telegram-desktop -- "${telegramUrl}"`;
    }
    
    exec(command, (error) => {
        if (error) {
            vscode.window.showErrorMessage(`Ошибка открытия Telegram: ${error.message}`);
            vscode.env.clipboard.writeText(text).then(() => {
                vscode.window.showInformationMessage('Код скопирован в буфер - вставьте в Telegram');
            });
        } else {
            vscode.window.showInformationMessage('Telegram открыт - отправьте сообщение себе');
        }
    });
}
function deactivate() {}

module.exports = {
    activate,
    deactivate
};