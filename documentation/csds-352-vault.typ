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
    #align(center + horizon, [
      #image("images/capstone/logo.png", width: 40%)
    ])
  ]
)


#layoutA(
  content: [
    = Did you know?
    
    #v(10pt)

    #contentBox(
      fill: theme.primaryLightest,
      text(
        fill: white,
        size: 24pt,
        [
          DANE explained that last year, 39.6% of households owned their homes. 
          Of the national total, 36% have paid off their homes in full, 
          while 3.5% of families live in their own homes but are still paying for them.
        ],
      ),
    )   
    #text(size: 15pt, fill: black, "https://www.larepublica.co/economia/cuatro-de-cada-10-hogares-en-colombia-son-duenos-de-su-vivienda-4118757") 

    #v(10pt) 

    #contentBox(
      fill: theme.primaryLightest,
      text(
        fill: white,
        size: 24pt,
        [
          The FNA (Fondo Nacional del Ahorro) will finance up to 90% of 
          mortgage loans throughout the country.
        ],
      ),
    )
    #text(size: 15pt, fill: black, "https://www.fna.gov.co/prensa/boletines-de-prensa/cumple-tu-sueno-de-vivienda-propia-en-el-fna
") 
  ]
)

#layoutC(
  title: "",
  content: [
    #align(center + horizon, [
      #text(
        size: 30pt,
        weight: "bold",
        fill: theme.primary,
        [
          So, if there are benefits and opportunities,  
          why do so many Colombians still not take the step towards owning a home?
        ],
      )
    ])
  ]
)

#layoutC(
  title: "The answer lies in lack of knowledge and, of course, in their budget",
  content: [
    
    #v(20pt)

    #text(
      size: 30pt,
      [
        - Many families do not know which subsidies they can apply for.
        - They are unaware of the types of housing available.
        - They confuse the different kinds of mortgage loans.
        - They believe myths, such as renting being cheaper than buying.
      ]
    )
  ]
)

#layoutC(
  title: "The solution: MiCasaBot",
  content: [
    
    #v(10pt)

    #text(size: 28pt)[
      “MiCasaBot is a chatbot that responds clearly, quickly, and with verified information 
      from official sources such as the Ministry of Housing, decrees, articles, and laws…”
    ]

    #v(20pt)

    #text(size: 28pt)[
      == Users can ask in simple language:

      #v(10pt)

      - What subsidies can I apply for?
      - What is the difference between a mortgage loan and leasing?
      - What percentage of the house must I have as a down payment?
    ]
  ]
)

#layoutC(
  title: "But why could this project interest you?",
  content: [
    #contentBox(
      fill: theme.primaryLightest,
      text(
        size: 30pt,
        fill: white,
        [
          MiCasaBot not only helps people with clear information,  
          but in the future it also aims to collect insights about the topics 
          that generate the most questions.  
          
          #v(15pt)

          This data would be valuable for governments, banks, real estate companies, 
          and housing projects to better understand Colombians’ needs 
          and attract more people.
        ]
      )
    )
  ]
)

#layoutC(
  title: "What is its architecture like?",
  content: [
    #align(center, [
      #image("images/capstone/C4_container.png", width: 100%)])
  ]
)

#layoutC(
  title: "",
  content: [
    #align(center + horizon, [
      #text(
        size: 40pt,
        weight: "bold",
        fill: theme.primary,
        [
          “Buying a home in Colombia should not be a mystery.”
        ],
      )
    ])
  ]
)