# This program will convert question and answer document into html page, for test page generation
# Foramt of 
data=open("ques.txt","r")
out=open("ques.xml","w")

for line in data:
    if len(line.split())<=0 or "#"==line[0] :
        continue
    else:
        # first thing in line is always a question
        ques=line.split("::")[0] 
        out.write("\n<Question>\n")
        out.write(ques+'\n')
        for opt in line.split("::")[1].split(): # Options are after questions
            out.write("\t<option> "+opt +"</option>")
            out.write("\n")
        out.write("</Question>")
data.close()
out.close()

