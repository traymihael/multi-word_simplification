import urllib.request

response = urllib.request.urlopen(
    'https://eikaiwa.weblio.jp/column/phrases/handy_english_phrases/useful-english-proverbs-and-sayings')
content = response.readline()
content = content.decode('utf-8')

print(content)
f = open('test.txt', 'w')

while content:
    flg = 0
    '''
    if '<p>' in content and '</p>' in content:
        # content = content.encode('utf-8')
        content = content.replace('</p>', '')
        content = content.split('<p>')

        f.write(content[1])
    '''
    if '</a></span></h3>' in content:
        flg = 1
        ans = []
        content = content.replace('</a></span></h3>', '')
        content = content.replace('\n', '')
        content = content.split('>')
        if '.' in content[-1]:
            content[-1] = content[-1].replace('.', '')
        ans.append(content[-1])

        content = response.readline()
        content = content.decode('utf-8')

        if '</a></span></h3>' not in content:

            if '<p>' in content and '</p>' in content:
                # content = content.encode('utf-8')
                content = content.replace('</p>', '')
                content = content.split('<p>')
                ans.append(content[-1])
                content = response.readline()
                content = content.decode('utf-8')

        f.write(ans[0])
        f.write('*')
        f.write(ans[1])
        print(ans)
    if flg == 0:
        content = response.readline()
        content = content.decode('utf-8')

f.close()
