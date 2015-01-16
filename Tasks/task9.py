#! /usr/bin/dev python
# -*- coding:utf8 -*-
def file_read(file_path):
	text=''
	for line in open(file_path,'r'):
		text += line.replace('\r','').replace('\n','').replace('\t','')
	return text

def split_body(text):
	return text[text.find('<body>')+len('<body>'):text.find('</body>')]

def html_reader(text,ftr=[],frm=True):
	output = '' # Результат / Вывод
	reader = '' # Прочитаный текст в теге
	filtring = len(ftr)!=0;

	tags = list() # Тэги    tags[-1] - последний тег
	tag_name = ''; # Имя тега
	tag_type = 0; # 0-не тег # 1- начало тега # 2-конец тега

	tag_read_name = False
	reading = False
	last_c = ''
	last_tag = ''
	last_tag2 = ''
	for c in text:
		# Форматирование
		def tag_format(tag):
			out = ''
			
			if tag_type==1: # открывающий тег <tag>
				#print 'open:',tag
				if tag=='td': out='\t'
				if tag=='tr' or tag=='table': out='\n'
				if tag=='li': out='\n *\t'
				if tag=='a': out='\n $'
				if tag=='div': out='\n\n/'+'-'*40
				if tag=='h1' or tag=='h2' or tag=='h3' or tag=='h4' or tag=='h5' or tag=='h6': out='\n'; print 'bhx'

			if tag_type==2: # закрывающий тег </tag>
				#print 'close',tag
				if tag=='ul': out='\n'
				if tag=='h1' or tag=='h2' or tag=='h3' or tag=='h4' or tag=='h5' or tag=='h6': out='\n'; print 'ehx'
				if tag=='div': out='\n\\'+'-'*40+'\n'

			if tag_type==3: # одиночный тег <tag/>
				#print 'single',tag
				if tag=='img': out='[image]'
				if tag=='hr': out='\n'+'-'*40+'\n'
				if tag=='br': out='\n'
			return out

		# Распознание тегов
		if c == '<' and not tag_read_name: 
			tag_read_name=True; reading=True
			tag_type=1
		elif c == '/' and last_c=='<' and tag_read_name: 
			tag_type=2
		elif c==' ' and tag_read_name and reading: reading=False
		elif c == '>' and tag_read_name:
			if last_c=='/':
				if tag_name[-1]=='/':tag_name=tag_name[:-1];
				tag_type=3
			if (filtring and tag_name in ftr) or not filtring:
				if tag_type==1: tags.append(tag_name)
				if tag_type==2: tags.pop(); output+=reader;
				if frm: output+=tag_format(tag_name)
			last_tag2 = last_tag; last_tag = tag_name; tag_name=''
			print reader
			reader = ''
			tag_type=0
			tag_read_name = False; reading=False

		# Чтение из текста
		elif tag_read_name:
			if reading:tag_name+=c
		else:
			#print 'tags: ',len(tags), tags
			if len(tags)==0 and not filtring: output+=c
			else: reader+=c
		last_c = c;
	return output

if __name__ == '__main__':
	html = split_body(file_read("index.html"))
	with open("index.txt",'w') as f:
		f.write(html_reader(html,ftr=["h1","h4","h3"],frm=False))