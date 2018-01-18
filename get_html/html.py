import urllib.request
response = urllib.request.urlopen('https://eikaiwa.weblio.jp/column/phrases/handy_english_phrases/useful-english-proverbs-and-sayings')
content = response.readline()
content = content.decode('utf-8')

print(content)
f = open('test.txt','w')

while content:

    if '<p>' in content and '</p>' in content:
        #content = content.encode('utf-8')
        content = content.replace('</p>', '')
        content = content.split('<p>')
    
        f.write(content[1])

    if '</a></span></h3>' in content:
        content = content.replace('</a></span></h3>', '')
        content = content.split('>')

        '''
        while '</a></span></h3>' not in content:
            content2 = response.readline()
            content2 = content2.decode('utf-8')
            if '<p>' in content2 and '</p>' in content2:
                # content = content.encode('utf-8')
                content2 = content2.replace('</p>', '')
                content2 = content2.split('<p>')
                content += content2
        '''
        f.write(content[-1])

    content = response.readline()
    content = content.decode('utf-8')
f.close()
