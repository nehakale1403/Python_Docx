from mailmerge import MailMerge
with MailMerge('words.docx') as document:
	document.merge_rows('col1',
                    [{'col1': 'Row 1, Column 1', 'col2': 'Row 1 Column 1'},
                     {'col1': 'Row 2, Column 1', 'col2': 'Row 2 Column 1'},
                     {'col1': 'Row 3, Column 1', 'col2': 'Row 3 Column 1'}])
	document.write(f'output.docx')