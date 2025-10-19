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
  title: "Agenda",
  content: [
    #v(20pt)
    #text(
      size: 28pt,
      [
        1. Introduction
        2. Identified Problem
        3. Proposed Solution
        4. Demonstration
        5. Benefits and Conclusions
      ]
    )
  ]
)

#layoutC(
  title: "Introduction",
  content: [
    === Did you know?

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
    #text(size: 15pt,fill: black,"https://www.larepublica.co/economia/cuatro-de-cada-10-hogares-en-colombia-son-duenos-de-su-vivienda-4118757")

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
    #text(size: 15pt,fill: black,"https://www.fna.gov.co/prensa/boletines-de-prensa/cumple-tu-sueno-de-vivienda-propia-en-el-fna")
  ]
)

#layoutC(
  title: "Identified Problem",
  content: [
    #align(center + horizon,
    [
      #text(
        size: 30pt,
        weight: "bold",
        fill: theme.primary,
        [
          So, if there are benefits and opportunities, why are so many Colombians not encouraged to buy a home?
        ],
      )
    ])
  ]
)

#layoutA(
  content: [
    #v(20pt)
    #text(
      size: 30pt,
      [
        The answer lies in lack of knowledge and, of course, in their budget

        - Many families do not know which subsidies they can apply for.
        - They are unaware of the types of housing available.
        - They confuse the different kinds of mortgage loans.
        - They believe myths, such as renting being cheaper than buying.
      ]
    )
  ]
)


#layoutC(
  title: "Proposed Solution",
  content: [
    #align(center + horizon,
    [
      #image("images/capstone/logo.png", width: 40%)
    ])
  ]
)

#layoutA(
  content: [
    #v(10pt)
    #text(size: 28pt)[
      “MiCasaBot is a chatbot that responds clearly, quickly, and with verified information
      from official sources such as the Ministry of Housing, decrees, articles, and laws…”
    ]

    #v(50pt)

    #grid(
      columns: (1fr, 1fr),
      gutter: 0.4in,
      [
        #align(center)[#image("images/capstone/source_1.png", width: 80%)]
      ],
      [
        #align(center)[#image("images/capstone/source_2.png", width: 80%)]
      ],
    )

    #v(20pt)

    #text(size: 28pt)[
      == Users can ask in simple language:
      #v(10pt)
      - What subsidies can I apply for?
      - What is mortgage leasing?
      - What percentage of the house must I have as a down payment?
    ]
  ]
)

#layoutC(
  title: "What’s inside MiCasaBot?",
  content: [
    #image("images/capstone/main_chat.png", width: 80%)
    == About the project
    #image("images/capstone/about_project.png", width: 100%)

    == Resources used by the bot
    #image("images/capstone/sources.png", width: 80%)

    == Data Visualization
    #image("images/capstone/data_visualization.png", width: 74%)
  ]
)

#layoutC(
  title: "How does it work?",
  content: [
    #align(center + horizon,
    [
      #image("images/capstone/architecture.png", width: 75%)
    ])
  ]
)

#layoutC(
  title: "Tech Stack",
  content: [
    #v(30pt)
    #grid(
      columns: (1fr,1fr),
      gutter: 0.4in,
      [
        #align(center)[#image("images/capstone/google_embedings_logo.png", width: 50%)]
      ],
      [
        #align(center)[#image("images/capstone/langchain_logo.png", width: 50%)]
      ],
      [
        #align(center)[#image("images/capstone/chroma_logo.png", width: 20%)]
      ],
      [
        #align(center)[#image("images/capstone/streamlit_logo.png", width: 50%)]
      ],
      [
        #align(center)[#image("images/capstone/gemini_logo.png", width: 50%)]
      ],
      [
        #align(center)[#image("images/capstone/fastapi_logo.png", width: 50%)]
      ],
    )
  ]
)

#layoutA(
  content: [
    #align(center + horizon,
    [
      #text(
        size: 50pt,
        weight: "bold",
        fill: theme.primary,
        [
          Demonstration
        ],
      )
    ])
  ]
)

#layoutC(
  title: "Benefits and Conclusions",
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

#layoutA(
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
