# LLM-app
* ```
  ! pip install langchain
  ! pip install dotenv
  ! pip install pypdf

* ```
  from langchain.document_loaders import PyPDFLoader
  loader = PyPDFLoader("/content/fundamental_rights_upsc.pdf")
  pages = loader.load()
* ```
  len(pages)
  page = pages[0]
  print(page.page_content[0:100])
  page.metadata
* ```
  from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
  chunk_size =500
  chunk_overlap = 0
* ```
  r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
  )
  c_splitter = CharacterTextSplitter(
      chunk_size=chunk_size,
      chunk_overlap=chunk_overlap
  )
* ```
  r_splitter.split_text(page.page_content)
  c_splitter.split_text(page.page_content)
