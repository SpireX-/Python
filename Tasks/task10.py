import task9
import sys

if __name__ == '__main__':
	if len(sys.argv)==3:
		html = task9.split_body(task9.file_read(sys.argv[1]))
		headers_alert = "\n<script>alert(\"%s\");</script>"%task9.html_reader(html,ftr=["h1","h2","h3","h4","h5","h6"]).replace("\n\n","\n").replace("\n","\\n")

		f_source = open(sys.argv[1],'r');
		f_output = open(sys.argv[2],'w');

		for line in f_source:
			if "</body>" in line:
				body_pos = line.find("</body>")
				line = line[:body_pos]+headers_alert+line[body_pos:]
				f_output.write( line )
			else: f_output.write( line )

		f_source.close();
		f_output.close();

	else:
		print "Error :)\ntask10.py source output"