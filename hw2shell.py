#output_file = open('about.html', 'w+')
#top_file = open('3_templates/top.html', 'r+')
#output_file.write('hello world')
#output_file.close()
#ab= open('about.html','w+')
#ab=open('about.html', 'a+')



# Open & read top
top = open('templates/top.html').read()
# Open & read contents
about_content = open('content/about.html').read()
# Open & read bottom
bottom = open('templates/bottom.html').read()
# Concatenate top, contents and bototm
about_file = top + about_content + bottom
# Open & write results
open('docs/about.html', 'w+').write(about_file)


# Open & read top
# Open & read contents
blog_content = open('content/blog.html').read()
# Open & read bottom
# Concatenate top, contents and bototm
blog_file = top + blog_content + bottom
# Open & write results
open('docs/blog.html', 'w+').write(blog_file)

# Open & read top
# Open & read contents
contact_content = open('content/contact.html').read()
# Open & read bottom
# Concatenate top, contents and bototm
contact_file = top + contact_content + bottom
# Open & write results
open('docs/contact.html', 'w+').write(contact_file)

# Open & read top
# Open & read contents
index_content = open('content/index.html').read()
# Open & read bottom
# Concatenate top, contents and bototm
index_file = top + index_content + bottom
# Open & write results
open('docs/index.html', 'w+').write(index_file)

