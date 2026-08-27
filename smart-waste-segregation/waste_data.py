# waste_data.py - Waste Database for EcoSort
# Based on CPCB Guidelines 2016
# Source: https://cpcb.nic.in

WASTE_DATABASE = {
    "organic": {
        "name": "Organic / Wet Waste",
        "color": "#10b981",
        "icon": "fa-seedling",
        "bin_color": "Green Bin",
        "items": {
            "banana peel": {
                "description": "Peel from banana fruit",
                "recycling_method": "Composting - add to kitchen compost bin",
                "decomposition_time": "2-3 weeks",
                "environmental_impact": "Rich in potassium and phosphorus, excellent for plants",
                "recycling_process": "Collect in compost bin > Mix with dry leaves > Turn every 3 days > Ready in 2-3 weeks"
            },
            "apple core": {
                "description": "Core and seeds from apple",
                "recycling_method": "Composting or vermicomposting",
                "decomposition_time": "1-2 months",
                "environmental_impact": "Contains natural sugars that attract insects if not composted",
                "recycling_process": "Chop into small pieces > Add to compost pile > Cover with brown material > Decomposes naturally"
            },
            "orange peel": {
                "description": "Peel from orange, lemon, citrus fruits",
                "recycling_method": "Composting or dried for cleaning agents",
                "decomposition_time": "3-6 months",
                "environmental_impact": "Citric acid can help break down other organic matter",
                "recycling_process": "Dry the peels > Grind to powder > Use as natural cleaner or compost"
            },
            "vegetable peels": {
                "description": "Peels from potato, carrot, onion, etc.",
                "recycling_method": "Composting or vermicomposting",
                "decomposition_time": "2-4 weeks",
                "environmental_impact": "Natural organic matter that enriches soil",
                "recycling_process": "Collect daily > Add to compost bin with dry leaves > Turn weekly > Ready in 4-6 weeks"
            },
            "fruit peels": {
                "description": "Peels from mango, papaya, watermelon",
                "recycling_method": "Composting or dried for potpourri",
                "decomposition_time": "2-4 weeks",
                "environmental_impact": "Rich in nutrients for compost",
                "recycling_process": "Cut into small pieces > Mix with soil > Add composting bacteria > Decomposes in 2-3 weeks"
            },
            "tea leaves": {
                "description": "Used tea leaves and tea bags",
                "recycling_method": "Add to compost bin or use as garden fertilizer",
                "decomposition_time": "2-3 weeks",
                "environmental_impact": "Rich in nitrogen, good for soil",
                "recycling_process": "Dry the used leaves > Mix with soil > Use as nitrogen-rich fertilizer"
            },
            "coffee grounds": {
                "description": "Used coffee powder and filters",
                "recycling_method": "Composting or use as odor absorber",
                "decomposition_time": "2-4 weeks",
                "environmental_impact": "Good nitrogen source for compost",
                "recycling_process": "Collect in container > Add to compost pile > Mix with brown waste > Ready in 3-4 weeks"
            },
            "rice": {
                "description": "Cooked or uncooked rice waste",
                "recycling_method": "Composting",
                "decomposition_time": "2-3 weeks",
                "environmental_impact": "Breaks down quickly in compost",
                "recycling_process": "Add to compost bin > Cover with dry leaves > Decomposes naturally"
            },
            "bread": {
                "description": "Stale bread, bakery waste",
                "recycling_method": "Composting or donate if fresh",
                "decomposition_time": "1-2 weeks",
                "environmental_impact": "Food waste contributes to greenhouse gases",
                "recycling_process": "Break into pieces > Add to compost bin > Cover with soil > Decomposes quickly"
            },
            "egg shells": {
                "description": "Broken egg shells from kitchen",
                "recycling_method": "Grind and add to soil as calcium supplement",
                "decomposition_time": "1-2 weeks",
                "environmental_impact": "Natural source of calcium for plants",
                "recycling_process": "Wash and dry shells > Grind to powder > Mix with soil > Provides calcium to plants"
            },
            "fish bones": {
                "description": "Bones from fish after cooking",
                "recycling_method": "Composting (in deep pit) or dispose in organic bin",
                "decomposition_time": "1-2 months",
                "environmental_impact": "Rich in phosphorus but may attract animals",
                "recycling_process": "Bury deep in compost pit > Cover with soil > Decomposes slowly > Rich in minerals"
            },
            "meat scraps": {
                "description": "Small pieces of raw or cooked meat",
                "recycling_method": "Dispose in organic bin, avoid home composting",
                "decomposition_time": "1-3 months",
                "environmental_impact": "Attracts pests if not properly contained",
                "recycling_process": "Seal in biodegradable bag > Dispose in green bin > Municipal composting facility processes it"
            },
            "milk": {
                "description": "Expired milk, stale milk",
                "recycling_method": "Pour down drain with water or dispose in organic bin",
                "decomposition_time": "1-2 weeks",
                "environmental_impact": "Can attract animals and insects",
                "recycling_process": "Dilute with water > Pour down drain > Or add to compost pit"
            },
            "curd": {
                "description": "Expired yogurt, buttermilk",
                "recycling_method": "Dispose in organic bin",
                "decomposition_time": "1-2 weeks",
                "environmental_impact": "Dairy products decompose faster than meat",
                "recycling_process": "Add to compost bin > Mix with dry waste > Decomposes naturally"
            },
            "flowers": {
                "description": "Wilted flowers, floral waste",
                "recycling_method": "Composting or vermicomposting",
                "decomposition_time": "1-2 weeks",
                "environmental_impact": "Can be composted to reduce landfill waste",
                "recycling_process": "Collect wilted flowers > Add to compost pile > Turn regularly > Ready in 2 weeks"
            },
            "leaves": {
                "description": "Dry and wet leaves from garden",
                "recycling_method": "Use for mulching or composting",
                "decomposition_time": "3-6 months",
                "environmental_impact": "Natural mulch protects soil and retains moisture",
                "recycling_process": "Collect leaves > Shred if possible > Layer for mulch or compost > Rich organic matter"
            },
            "grass clippings": {
                "description": "Freshly cut grass from lawn",
                "recycling_method": "Composting or leave as mulch",
                "decomposition_time": "1-2 months",
                "environmental_impact": "High nitrogen content, good for compost",
                "recycling_process": "Spread thinly to dry > Add to compost bin > Mix with brown waste > Quick decomposition"
            },
            "garden waste": {
                "description": "Small branches, twigs, weeds",
                "recycling_method": "Composting or green waste collection",
                "decomposition_time": "2-6 months",
                "environmental_impact": "Returns nutrients to soil",
                "recycling_process": "Chop into small pieces > Add to compost heap > Turn monthly > Use in garden"
            },
            "coconut shell": {
                "description": "Coconut shells and husks",
                "recycling_method": "Can be used for crafts or slow composting",
                "decomposition_time": "6-12 months",
                "environmental_impact": "Very hard, takes long to decompose naturally",
                "recycling_process": "Dry the shell > Use for crafts or decorations > Or chip and compost slowly"
            },
            "corn husks": {
                "description": "Outer covering of corn",
                "recycling_method": "Composting or use as wrapping material",
                "decomposition_time": "2-3 months",
                "environmental_impact": "Biodegradable and compostable",
                "recycling_process": "Dry and shred > Add to compost pile > Decomposes naturally"
            },
            "sugarcane bagasse": {
                "description": "Fibrous residue after juice extraction",
                "recycling_method": "Composting or use as biomass fuel",
                "decomposition_time": "3-4 months",
                "environmental_impact": "Renewable resource, can replace wood",
                "recycling_process": "Dry thoroughly > Compost or use as fuel > Reduces deforestation"
            },
            "pizza box": {
                "description": "Greasy cardboard from food packaging",
                "recycling_method": "Compost (food-soiled paper cannot be recycled)",
                "decomposition_time": "2-3 months",
                "environmental_impact": "Food contamination makes paper non-recyclable",
                "recycling_process": "Tear into pieces > Add to compost bin > Grease helps decomposition"
            },
            "tea bag": {
                "description": "Used tea bags including string",
                "recycling_method": "Remove staple and compost the bag",
                "decomposition_time": "1-2 months",
                "environmental_impact": "Some tea bags contain microplastics",
                "recycling_process": "Remove staple > Open bag > Empty leaves to compost > Bag may take longer"
            },
            "napkins": {
                "description": "Used paper napkins and tissues",
                "recycling_method": "Compost if not heavily soiled",
                "decomposition_time": "2-4 weeks",
                "environmental_impact": "Paper products should not go to landfill",
                "recycling_process": "Add to compost bin > Breaks down quickly > Returns nutrients to soil"
            },
            "food scraps": {
                "description": "Leftover food, mixed food waste",
                "recycling_method": "Home composting or municipal collection",
                "decomposition_time": "2-4 weeks",
                "environmental_impact": "Major source of methane in landfills",
                "recycling_process": "Separate from packaging > Compost at home > Or give to green bin collection"
            },
            "pasta": {
                "description": "Cooked or raw pasta waste",
                "recycling_method": "Composting",
                "decomposition_time": "1-2 weeks",
                "environmental_impact": "Starch breaks down quickly",
                "recycling_process": "Add to compost bin > Mix with soil > Decomposes in 1-2 weeks"
            },
            "onion peels": {
                "description": "Outer layers of onion",
                "recycling_method": "Composting or natural dye",
                "decomposition_time": "2-3 weeks",
                "environmental_impact": "Rich in antioxidants, good for compost",
                "recycling_process": "Collect peels > Add to compost or boil for natural dye > Eco-friendly"
            },
            "potato peels": {
                "description": "Skin removed from potatoes",
                "recycling_method": "Composting or make crispy chips",
                "decomposition_time": "2-3 weeks",
                "environmental_impact": "High in starch, decomposes quickly",
                "recycling_process": "Wash and compost > Or fry for snacks > Zero waste approach"
            },
            "garlic skin": {
                "description": "Outer papery skin of garlic",
                "recycling_method": "Composting",
                "decomposition_time": "1-2 weeks",
                "environmental_impact": "Thin and decomposes quickly",
                "recycling_process": "Collect garlic skin > Add to compost bin > Breaks down in days"
            },
            "jaggery": {
                "description": "Expired or hardened jaggery",
                "recycling_method": "Composting",
                "decomposition_time": "1-2 weeks",
                "environmental_impact": "Natural sweetener, decomposes quickly",
                "recycling_process": "Break into pieces > Add to compost > Rich in minerals for soil"
            }
        }
    },
    "recyclable": {
        "name": "Recyclable / Dry Waste",
        "color": "#3b82f6",
        "icon": "fa-recycle",
        "bin_color": "Blue Bin",
        "items": {
            "newspaper": {
                "description": "Old newspapers, daily papers",
                "recycling_method": "Send to paper recycling centers or local waste dealers",
                "decomposition_time": "2-6 weeks (if not recycled)",
                "environmental_impact": "Recycling 1 ton of paper saves 17 trees",
                "recycling_process": "Collect and bundle > Send to recycler > Pulped with water > Made into new paper products"
            },
            "magazine": {
                "description": "Old magazines, brochures",
                "recycling_method": "Paper recycling centers",
                "decomposition_time": "1-2 weeks",
                "environmental_impact": "Glossy paper requires special recycling",
                "recycling_process": "Remove plastic covers > Stack and bundle > Send to recycler > Re-pulped into new paper"
            },
            "cardboard": {
                "description": "Corrugated boxes, packaging material",
                "recycling_method": "Flatten and send to recycling centers",
                "decomposition_time": "2 months",
                "environmental_impact": "Can be recycled 5-7 times",
                "recycling_process": "Flatten boxes > Remove tape and staples > Bundle > Recycler pulps and makes new cardboard"
            },
            "plastic bottle": {
                "description": "PET bottles, water bottles, soft drink bottles",
                "recycling_method": "Send to plastic recycling units",
                "decomposition_time": "450+ years (if not recycled)",
                "environmental_impact": "Takes centuries to decompose, harms marine life",
                "recycling_process": "Rinse bottles > Remove caps > Send to recycler > Melted and spun into polyester fiber"
            },
            "glass bottle": {
                "description": "Glass bottles, jars",
                "recycling_method": "Send to glass recycling centers, handle carefully",
                "decomposition_time": "1 million+ years",
                "environmental_impact": "Can be recycled infinitely without loss of quality",
                "recycling_process": "Sort by color > Crush into cullet > Melt in furnace > Made into new glass products"
            },
            "metal can": {
                "description": "Aluminum cans, tin cans, steel containers",
                "recycling_method": "Send to metal scrap dealers or recycling centers",
                "decomposition_time": "80-200 years",
                "environmental_impact": "Recycling aluminum uses 95% less energy than new production",
                "recycling_process": "Crush cans > Sort by metal type > Melt in furnace > Made into new cans or products"
            },
            "aluminum foil": {
                "description": "Used aluminum foil, wrapping foil",
                "recycling_method": "Clean and send to metal recycling",
                "decomposition_time": "200+ years",
                "environmental_impact": "Infinitely recyclable material",
                "recycling_process": "Clean off food residue > Ball up foil > Send to recycler > Melted and recycled"
            },
            "clothes": {
                "description": "Old clothes, fabric scraps, rags",
                "recycling_method": "Donate to charities or textile recycling centers",
                "decomposition_time": "6 months to 1 year",
                "environmental_impact": "Textile waste is a major pollution source",
                "recycling_process": "Sort by condition > Donate wearable clothes > Recycle worn-out into rags or insulation"
            },
            "shoes": {
                "description": "Old shoes, sandals, slippers",
                "recycling_method": "Donate or send to specialized shoe recyclers",
                "decomposition_time": "30-40 years",
                "environmental_impact": "Synthetic materials take very long to decompose",
                "recycling_process": "Separate materials > Rubber soles to recycler > Uppers for donation > Reduce landfill waste"
            },
            "notebook": {
                "description": "Used notebooks, loose papers",
                "recycling_method": "Paper recycling, remove spiral binding first",
                "decomposition_time": "2-6 weeks",
                "environmental_impact": "Paper recycling saves water and energy",
                "recycling_process": "Remove spiral/staples > Stack paper > Send to recycler > Pulped into new paper"
            },
            "plastic bag": {
                "description": "Shopping bags, carry bags",
                "recycling_method": "Return to stores or send to plastic recyclers",
                "decomposition_time": "500-1000 years",
                "environmental_impact": "Major source of plastic pollution, kills marine animals",
                "recycling_process": "Collect and clean > Send to recycler > Melted into pellets > Made into new plastic products"
            },
            "plastic container": {
                "description": "Food containers, tubs, buckets",
                "recycling_method": "Rinse and send for plastic recycling",
                "decomposition_time": "100+ years",
                "environmental_impact": "Plastic pollution if not recycled",
                "recycling_process": "Rinse thoroughly > Sort by plastic type > Send to recycler > Processed into new items"
            },
            "tin can": {
                "description": "Food tins, oil cans, paint tins",
                "recycling_method": "Rinse and send to metal recycling",
                "decomposition_time": "80-200 years",
                "environmental_impact": "Metal is highly recyclable",
                "recycling_process": "Rinse clean > Remove labels > Crush to save space > Melt and recycle into new metal"
            },
            "steel": {
                "description": "Steel utensils, iron rods, scrap metal",
                "recycling_method": "Send to metal scrap dealer",
                "decomposition_time": "100+ years",
                "environmental_impact": "Steel recycling saves 74% energy vs new production",
                "recycling_process": "Collect scrap > Sort by type > Melt in electric furnace > Rolled into new steel products"
            },
            "copper": {
                "description": "Copper wires, pipes, utensils",
                "recycling_method": "Send to specialized metal recyclers",
                "decomposition_time": "Does not corrode easily",
                "environmental_impact": "Copper is 100% recyclable without quality loss",
                "recycling_process": "Strip wire insulation > Sort by purity > Melt and refine > Used in new electrical products"
            },
            "mobile phone": {
                "description": "Old phones, broken handsets",
                "recycling_method": "E-waste recyclers only, contains valuable metals",
                "decomposition_time": "1000+ years",
                "environmental_impact": "Contains gold, silver, copper but also toxic materials",
                "recycling_process": "Remove battery > Send to authorized recycler > Precious metals recovered > Toxic materials safely disposed"
            },
            "laptop": {
                "description": "Old laptops, broken computers",
                "recycling_method": "E-waste recyclers, contains hazardous materials",
                "decomposition_time": "1000+ years",
                "environmental_impact": "Contains lead, mercury, cadmium",
                "recycling_process": "Data wipe > Remove battery > Send to certified recycler > Components separated and recycled"
            },
            "charger": {
                "description": "Phone chargers, laptop chargers",
                "recycling_method": "E-waste collection centers",
                "decomposition_time": "500+ years",
                "environmental_impact": "Contains copper wire and plastic",
                "recycling_process": "Cut wire > Separate copper from plastic > Each material recycled separately"
            },
            "headphones": {
                "description": "Earphones, headphones, speakers",
                "recycling_method": "E-waste collection points",
                "decomposition_time": "500+ years",
                "environmental_impact": "Mixed materials, hard to separate",
                "recycling_process": "Send to e-waste recycler > Materials separated > Copper, plastic, rubber recycled"
            },
            "pen": {
                "description": "Empty pens, broken pens",
                "recycling_method": "Collect and send to pen recyclers or dispose carefully",
                "decomposition_time": "100+ years",
                "environmental_impact": "Plastic and ink, small but adds up",
                "recycling_process": "Collect used pens > Some brands have take-back programs > Otherwise dispose carefully"
            },
            "notebook": {
                "description": "Used notebooks, loose papers",
                "recycling_method": "Paper recycling, remove spiral binding first",
                "decomposition_time": "2-6 weeks",
                "environmental_impact": "Paper recycling saves water and energy",
                "recycling_process": "Remove spiral/staples > Stack paper > Send to recycler > Pulped into new paper"
            },
            "paper": {
                "description": "Loose papers, printer paper, documents",
                "recycling_method": "Paper recycling centers",
                "decomposition_time": "2-6 weeks",
                "environmental_impact": "Recycling paper saves trees and water",
                "recycling_process": "Collect and stack > Remove any plastic > Send to recycler > Pulp and make new paper"
            },
            "thermocol": {
                "description": "Styrofoam packaging, thermocol pieces",
                "recycling_method": "Special recycling centers, very light so costly to transport",
                "decomposition_time": "500+ years",
                "environmental_impact": "Breaks into microplastics, very harmful",
                "recycling_process": "Collect and compress > Send to special facility > Melted into dense blocks > Reused"
            },
            "mirror": {
                "description": "Broken mirrors, old mirrors",
                "recycling_method": "Wrap carefully and dispose, mirror coating makes recycling hard",
                "decomposition_time": "1 million+ years",
                "environmental_impact": "Silver coating complicates recycling",
                "recycling_process": "Wrap broken pieces carefully > Label as sharp > Dispose in construction waste"
            }
        }
    },
    "hazardous": {
        "name": "Hazardous Waste",
        "color": "#ef4444",
        "icon": "fa-radiation",
        "bin_color": "Red Bin (Special Collection)",
        "items": {
            "battery": {
                "description": "AA, AAA, button cell, rechargeable batteries",
                "recycling_method": "Do NOT throw in regular bins. Send to designated collection points or e-waste centers",
                "decomposition_time": "100+ years",
                "environmental_impact": "Contains toxic chemicals like mercury, lead, cadmium that poison soil and water",
                "recycling_process": "Collect used batteries > Take to battery recycling point > Batteries are broken down > Toxic materials safely extracted"
            },
            "electronic waste": {
                "description": "Old phones, chargers, cables, circuits",
                "recycling_method": "Send to authorized e-waste recyclers only",
                "decomposition_time": "1000+ years",
                "environmental_impact": "Contains precious metals and toxic materials",
                "recycling_process": "Collect e-waste > Send to certified recycler > Manual dismantling > Precious metals recovered"
            },
            "paint": {
                "description": "Leftover paint, paint brushes with paint",
                "recycling_method": "Dry out and send to hazardous waste collection",
                "decomposition_time": "Hundreds of years",
                "environmental_impact": "Contains VOCs that pollute air and water",
                "recycling_process": "Dry paint completely > Send to hazardous waste facility > Solvents recovered > Metals recycled"
            },
            "medicine": {
                "description": "Expired medicines, used strips, syringes",
                "recycling_method": "Return to pharmacy or hospital for safe disposal",
                "decomposition_time": "Varies",
                "environmental_impact": "Can contaminate water supply and harm wildlife",
                "recycling_process": "Collect expired medicines > Return to pharmacy > Incinerated at high temperature > No water contamination"
            },
            "thermometer": {
                "description": "Mercury thermometers, broken glass thermometers",
                "recycling_method": "Handle with care, take to hospital or e-waste center",
                "decomposition_time": "Permanent (mercury is toxic)",
                "environmental_impact": "Mercury is extremely toxic and bioaccumulates",
                "recycling_process": "Do not touch mercury > Collect in sealed container > Specialized mercury recovery > Safe disposal"
            },
            "bulb": {
                "description": "CFL bulbs, fluorescent tubes, LED bulbs",
                "recycling_method": "Special recycling required, contain mercury (CFL), send to e-waste centers",
                "decomposition_time": "1000+ years",
                "environmental_impact": "CFL bulbs contain mercury vapor",
                "recycling_process": "Handle carefully (do not break) > Send to e-waste center > Mercury extracted > Glass and metal recycled"
            },
            "chemical": {
                "description": "Household chemicals, cleaning agents, pesticides",
                "recycling_method": "Take to hazardous waste disposal facility",
                "decomposition_time": "Varies greatly",
                "environmental_impact": "Can contaminate groundwater and soil",
                "recycling_process": "Keep in original container > Take to hazardous waste facility > Neutralized or incinerated safely"
            },
            "nail": {
                "description": "Rusted nails, sharp metal objects",
                "recycling_method": "Put in separate container, send to metal recycling",
                "decomposition_time": "10-50 years",
                "environmental_impact": "Physical hazard to waste workers",
                "recycling_process": "Collect in puncture-proof container > Label as sharp > Send to metal recycler > Melted and reused"
            },
            "sanitary pad": {
                "description": "Used sanitary napkins and tampons",
                "recycling_method": "Wrap separately, dispose in designated bins",
                "decomposition_time": "500-800 years",
                "environmental_impact": "Contains plastic and chemicals",
                "recycling_process": "Wrap in newspaper > Dispose in designated bin > Cannot be recycled > Incineration is best option"
            },
            "diaper": {
                "description": "Used baby diapers",
                "recycling_method": "Wrap and dispose in regular waste (not recyclable)",
                "decomposition_time": "500+ years",
                "environmental_impact": "Major contributor to landfill waste",
                "recycling_process": "Wrap securely > Dispose in regular waste > Cannot be recycled > Consider cloth diapers"
            },
            "razor": {
                "description": "Disposable razors, razor blades",
                "recycling_method": "Wrap blades safely and dispose, send razor handles to dry waste",
                "decomposition_time": "100+ years",
                "environmental_impact": "Sharp hazard, mixed materials",
                "recycling_process": "Wrap blade in cardboard > Label as sharp > Dispose carefully > Handle to dry waste"
            },
            "syringe": {
                "description": "Used syringes, injection needles",
                "recycling_method": "Use puncture-proof container, return to hospital or clinic",
                "decomposition_time": "100+ years",
                "environmental_impact": "Biohazard, risk of infection",
                "recycling_process": "Do not recap > Place in sharps container > Return to healthcare facility > Autoclaved and incinerated"
            },
            "tire": {
                "description": "Old vehicle tires, bicycle tires",
                "recycling_method": "Send to tire recyclers, can be made into rubber products",
                "decomposition_time": "50-80 years",
                "environmental_impact": "Major fire hazard, breeding ground for mosquitoes",
                "recycling_process": "Shred tires > Remove steel > Rubber granules > Used in roads, playgrounds, new tires"
            }
        }
    },
    "domestic_hazardous": {
        "name": "Domestic Hazardous Waste",
        "color": "#f59e0b",
        "icon": "fa-triangle-exclamation",
        "bin_color": "Red Bag / Special Collection",
        "items": {
            "oil": {
                "description": "Used cooking oil, motor oil",
                "recycling_method": "Collect and send to biodiesel producers or recycling centers",
                "decomposition_time": "Does not decompose easily",
                "environmental_impact": "Clogs drains, pollutes water bodies",
                "recycling_process": "Collect oil in container > Send to biodiesel producer > Processed into fuel > Or recycled into lubricants"
            },
            "cooking oil": {
                "description": "Used oil from frying and cooking",
                "recycling_method": "Collect in bottle, send to biodiesel maker",
                "decomposition_time": "Does not decompose",
                "environmental_impact": "Major drain clogger, water pollutant",
                "recycling_process": "Filter food particles > Collect in sealed container > Deliver to collection point > Biodiesel conversion"
            },
            "detergent": {
                "description": "Empty detergent bottles, cleaning product containers",
                "recycling_method": "Rinse and send for plastic recycling",
                "decomposition_time": "100+ years",
                "environmental_impact": "Chemical residues can contaminate water",
                "recycling_process": "Rinse thoroughly > Remove labels if possible > Send to plastic recycler > Made into new containers"
            },
            "shampoo": {
                "description": "Empty shampoo bottles, conditioners",
                "recycling_method": "Rinse and send for plastic recycling",
                "decomposition_time": "100+ years",
                "environmental_impact": "Plastic pollution if not recycled",
                "recycling_process": "Rinse bottle > Remove pump (different plastic) > Send to plastic recycler"
            },
            "soap": {
                "description": "Leftover soap pieces, soap wrappers",
                "recycling_method": "Collect small pieces and melt into new bar",
                "decomposition_time": "1-2 months",
                "environmental_impact": "Chemicals in soap affect aquatic life",
                "recycling_process": "Collect small pieces > Melt with water > Form new bar > Wrapper to dry waste"
            },
            "mosquito coil": {
                "description": "Used mosquito coils, repellent containers",
                "recycling_method": "Dispose carefully, coil residue is hazardous",
                "decomposition_time": "Varies",
                "environmental_impact": "Contains chemicals harmful to health",
                "recycling_process": "Ash from coils is toxic > Collect carefully > Dispose in hazardous waste > Use natural repellents"
            },
            "insecticide": {
                "description": "Empty insecticide cans, spray bottles",
                "recycling_method": "Triple rinse and send to hazardous waste",
                "decomposition_time": "100+ years",
                "environmental_impact": "Highly toxic to environment",
                "recycling_process": "Triple rinse container > Rinse water as pesticide > Container to hazardous waste > Never reuse for food"
            },
            "nail polish": {
                "description": "Empty nail polish bottles, nail polish remover",
                "recycling_method": "Hazardous waste, contains chemicals",
                "decomposition_time": "100+ years",
                "environmental_impact": "Contains acetone and chemicals",
                "recycling_process": "Dry out remaining polish > Dispose bottle in hazardous waste > Use water-based polish instead"
            },
            "perfume": {
                "description": "Empty perfume bottles, cologne",
                "recycling_method": "Glass bottles recyclable, spray mechanism to hazardous waste",
                "decomposition_time": "100+ years",
                "environmental_impact": "Alcohol and chemicals in residue",
                "recycling_process": "Remove spray mechanism > Glass bottle to recycling > Mechanism to hazardous waste"
            },
            "battery acid": {
                "description": "Leaked battery acid, battery parts",
                "recycling_method": "Handle with gloves, send to hazardous waste",
                "decomposition_time": "Permanent",
                "environmental_impact": "Highly corrosive, toxic",
                "recycling_process": "Wear gloves > Collect in sealed container > Take to hazardous waste facility > Neutralized safely"
            }
        }
    },
    "construction": {
        "name": "Construction & Demolition Waste",
        "color": "#8b5cf6",
        "icon": "fa-helmet-safety",
        "bin_color": "Construction Waste Collection",
        "items": {
            "brick": {
                "description": "Broken bricks, masonry pieces",
                "recycling_method": "Can be crushed and used as aggregate in construction",
                "decomposition_time": "Does not decompose",
                "environmental_impact": "Can be recycled into new building materials",
                "recycling_process": "Collect and crush > Sort by size > Use as aggregate in concrete > Reduces mining of natural stone"
            },
            "cement": {
                "description": "Dried cement bags, cement residue",
                "recycling_method": "Dispose at authorized construction waste facilities",
                "decomposition_time": "Does not decompose",
                "environmental_impact": "Contributes to landfill volume",
                "recycling_process": "Collect dried cement > Crush and grind > Use as filler material in construction"
            },
            "wood": {
                "description": "Scrap wood, sawdust, wood shavings",
                "recycling_method": "Can be used for particle board or biomass energy",
                "decomposition_time": "1-5 years",
                "environmental_impact": "Good source of biomass energy",
                "recycling_process": "Sort treated vs untreated > Untreated to biomass > Treated to special disposal > Sawdust for compost"
            },
            "tile": {
                "description": "Broken tiles, ceramic waste",
                "recycling_method": "Can be crushed and used in road construction",
                "decomposition_time": "Does not decompose",
                "environmental_impact": "Can be recycled into construction aggregate",
                "recycling_process": "Collect and crush > Use as road base material > Or as aggregate in concrete"
            },
            "steel reinforcement": {
                "description": "Rebar, steel rods, metal frames",
                "recycling_method": "Highly recyclable, send to steel recycler",
                "decomposition_time": "100+ years",
                "environmental_impact": "Steel recycling saves 74% energy",
                "recycling_process": "Collect scrap steel > Send to steel mill > Melted in electric furnace > Rolled into new rebar"
            },
            "concrete": {
                "description": "Broken concrete, cement blocks",
                "recycling_method": "Crush and use as recycled aggregate",
                "decomposition_time": "Does not decompose",
                "environmental_impact": "Reduces need for natural aggregate mining",
                "recycling_process": "Break into pieces > Crush in crusher > Sort by size > Use as road base or concrete aggregate"
            },
            "pipe": {
                "description": "PVC pipes, metal pipes, plumbing waste",
                "recycling_method": "Metal pipes recyclable, PVC to specialized facilities",
                "decomposition_time": "100+ years (PVC)",
                "environmental_impact": "PVC releases toxins when burned",
                "recycling_process": "Metal pipes to scrap dealer > PVC pipes to specialized recycler > Reuse when possible"
            },
            "glass": {
                "description": "Window glass, glass panels",
                "recycling_method": "Send to glass recycling, remove frames first",
                "decomposition_time": "1 million+ years",
                "environmental_impact": "Glass is infinitely recyclable",
                "recycling_process": "Remove from frames > Sort by color > Crush and melt > Made into new glass products"
            },
            "rubble": {
                "description": "Mixed construction debris",
                "recycling_method": "Sort and recycle each material separately",
                "decomposition_time": "Varies",
                "environmental_impact": "Mixed waste is harder to recycle",
                "recycling_process": "Sort into categories > Metal to scrap > Concrete to crusher > Wood to biomass > Reduce landfill"
            }
        }
    }
}

# Helper function to get all items flat
def get_all_items():
    all_items = []
    for category_key, category_data in WASTE_DATABASE.items():
        for item_key, item_data in category_data["items"].items():
            all_items.append({
                "name": item_key,
                "category": category_key,
                "category_name": category_data["name"],
                "data": item_data
            })
    return all_items

# Helper function to search items
def search_items(query):
    query_lower = query.lower().strip()
    results = []
    
    # Exact match first
    for category_key, category_data in WASTE_DATABASE.items():
        for item_key, item_data in category_data["items"].items():
            if item_key == query_lower:
                return [{
                    "name": item_key,
                    "category": category_key,
                    "category_name": category_data["name"],
                    "color": category_data["color"],
                    "bin_color": category_data.get("bin_color", ""),
                    "data": item_data
                }]
    
    # Partial match
    for category_key, category_data in WASTE_DATABASE.items():
        for item_key, item_data in category_data["items"].items():
            if query_lower in item_key or item_key in query_lower:
                results.append({
                    "name": item_key,
                    "category": category_key,
                    "category_name": category_data["name"],
                    "color": category_data["color"],
                    "bin_color": category_data.get("bin_color", ""),
                    "data": item_data
                })
    
    return results[:10]
