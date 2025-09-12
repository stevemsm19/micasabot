#import "common/lib/contentBox.typ": contentBox
#import "common/lib/slideLayouts.typ": theme, mainTitle, layoutA, layoutATwoCols, layoutATwoColsWithTitle, layoutBTwoCols, layoutC, layoutCTwoColsWithTitle, layoutDTwoCols

#mainTitle(
  title: "CSDS-352 Vault",
  subtitle: "Oscar Muñoz <oscar.munoz@jala.university>",
  content: [
    #v(160pt)
    #contentBox(
      fill: luma(150, 30%),
      text(
        fill: white,
        size: 20pt,
        [
          This is a companion document that contains notes and references for the *Machine Learning* course.
        ],
      ),
    )
  ],
)

#layoutC(
  title: "About my project",
  content: [
    #set text(size: 23pt)
    I chose to build an application in which users could find answers to questions related to a specific topic, namely *housing* here in Colombia, with the help of documents such as decrees, articles, laws, among others... which, although everyone has access to them, are difficult to find and not very user-friendly because there is so much content.

    This idea comes from a common problem I’ve identified in people who would like to buy a home but, due to lack of knowledge and, of course, financial reasons, they don’t. Nowadays, there are some subsidies and good interest rates in the market that can make it much easier to buy a home, however, this is not clear to everyone, and it’s not something that is usually mentioned when trying to buy a house. For example, what rights do we have as Colombians? What can we access depending on our profile? What subsidies can we apply for? What are those strange terms construction companies mention when selling a project, etc.....?
  ],
)


#layoutC(
  title: "Stack",
  content: [
    #set text(size: 23pt)
    - *Language:* Python
    - *Embedding model:* all-MiniLM-L6-v1
    - *Vector database:* Chroma
    - *Backend:* FastAPI
    - *Frontend:* Streamlit
  ]

)