from Auxiliary import Auxiliary
import Statement
import datetime

aux = Auxiliary()


try:
    fullpath, filename, file_extention = aux.getSourceStatementName()
    print (filename)
except AttributeError:
    exit(0)

acceptext = [".DBF", ".CSV"]


if file_extention not in acceptext:
    exit(0)


elif file_extention == ".CSV":

    statement = Statement.MarfinStatement()
elif file_extention == ".DBF":


    statement = Statement.PivdennyStatement()

suffix = statement.createOutDbfName()

outputDbfName = fullpath +"\\"+suffix.upper() + ".DBF"


table = statement.createEtalonDbf(outputDbfName)

statement.parse(filename)


for _ in range(10):
    info = ("test_ls", "test_nomerplat", 10.5, datetime.datetime.date(datetime.datetime.now()), "test_comment")
    statement.writeCortege(info, table)

statement.closeEtalonDfb(table)
