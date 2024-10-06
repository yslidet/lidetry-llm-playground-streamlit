import re
import html 

def process_markdown(text):
    text = html.escape(text)

    def replace_code_block(match):
        code = match.group(1).strip()
        return f'<pre><code>{code}</code></pre>'

    print(f'HTML before: {text}')
    text = re.sub(r'```([\s\S]*?)```', replace_code_block, text)
    text = re.sub(r'`([^`\n]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\n(?!<pre>|<code>|<\/pre>|<\/code>)', '<br>', text)
    print(f'HTML after: {text}')

    return text