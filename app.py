import streamlit as st
import time

# Inizializzazione di eventuali variabili di sessione mancanti
if "intro_seen" not in st.session_state:
    st.session_state.intro_seen = False
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "completed" not in st.session_state:
    st.session_state.completed = False
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "final" not in st.session_state:
    st.session_state.final = False

# Se il flag finale è True, mostra la pagina finale e interrompi l'esecuzione
if st.session_state.final:
    st.markdown("<h1 style='text-align: center;'>Lascia stare.</h1>", unsafe_allow_html=True)
    st.stop()

# Configurazione della pagina
st.set_page_config(page_title="Scopri che tipo di informatore sei", page_icon="💼", layout="centered")

# Stile CSS personalizzato
st.markdown("""
    <style>
        /* Sfondo generale */
        body {
            background-color: #f5f7fa;
        }
        .main {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        /* Stile della barra di avanzamento */
        .stProgress > div > div > div > div {
            background-color: #4CAF50 !important;
        }
        /* Stile del box della domanda */
        .question-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        /* Stile pulsanti */
        .stButton>button {
            background-color: #007BFF;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 10px;
            width: 100%;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Pagina introduttiva (mostrata solo la prima volta)
if not st.session_state.intro_seen:
    def start_test():
        st.session_state.intro_seen = True

    st.title("💼💊 Scopri che tipo di informatore sei!")
    st.markdown("""
        **Benvenuto al test di valutazione attitudinale**

        In questo questionario, studiato appositamente per il mondo degli informatori medici, potrai scoprire il tuo stile comunicativo e il modo in cui interagisci con i colleghi.  
        Il test è pensato per evidenziare le tue competenze relazionali e il tuo approccio strategico, confrontandoti con situazioni reali del settore.
        
        **Come funziona?**
        - Risponderai a una serie di domande che simulano scenari tipici del lavoro di informatore.
        - Ogni risposta contribuirà a definire il tuo profilo professionale e il modo in cui ti distingui rispetto agli altri.
        - Al termine, riceverai un’analisi personalizzata, basata sulle tue risposte, che ti aiuterà a comprendere meglio le tue attitudini e le aree di miglioramento.
        
        Sei pronto a scoprire il tuo vero profilo e a confrontarti con i tuoi colleghi?
    """)
    st.button("Inizia il test", on_click=start_test)
    st.stop()

# Dati del quiz con le nuove domande
quiz_data = [
    {
        "question": "Un collega ti contatta urgentemente perché non riesce a trovare lo studio del medico. Come rispondi alla sua richiesta?",
        "choices": [
            "Fornisci indicazioni precise e dettagliate, dimostrando pieno supporto.",
            "Dai indicazioni deliberatamente errate, indirizzandolo su un percorso fuorviante che lo porterà a perdersi.",
            "Suggerisci di consultare un’app di navigazione, offrendoti di assisterlo se necessario.",
            "Offri un percorso generico e poco curato, senza verificare se sia realmente funzionale, lasciando il collega in una situazione di incertezza."
        ]
    },
    {
        "question": "Durante la pausa pranzo, un collega esprime insoddisfazione per il rapporto con un medico. Qual è il tuo approccio?",
        "choices": [
            "Offri consigli basati sulla tua esperienza per migliorare la comunicazione.",
            "Proponi una strategia alternativa che, sebbene sembri valida, è studiata per fornire indicazioni errate e complicare ulteriormente il rapporto.",
            "Ascolti attentamente e suggerisci soluzioni pratiche per superare le difficoltà.",
            "Mostri una disponibilità superficiale, offrendo una risposta vaga che non contribuisce a chiarire il problema."
        ]
    },
    {
        "question": "Un nuovo membro del team, con minore esperienza, ti chiede consigli su come affrontare il lavoro quotidiano. Come rispondi?",
        "choices": [
            "Offri spiegazioni dettagliate e supporto pratico per agevolarne l’inserimento.",
            "Suggerisci un approccio non convenzionale che, pur apparendo innovativo, porta il collega a seguire una strada inefficace.",
            "Offri indicazioni estremamente sintetiche e poco approfondite, rischiando di lasciarlo in difficoltà.",
            "Lo indirizzi verso risorse e documentazione utile, stimolandolo all’autonomia."
        ]
    },
    {
        "question": "Osservi che un collega adotta una strategia simile alla tua per interagire con un medico, con il quale hai avuto difficoltà. Come reagisci?",
        "choices": [
            "Esprimi delle riserve e proponi una variante del tuo metodo, volutamente meno efficace, per distoglierlo dalla strategia corretta.",
            "Inviti il collega a un confronto costruttivo per condividere esperienze e migliorare insieme.",
            "Non ti impegni ad intervenire, lasciando il collega senza un supporto concreto e aumentando il rischio di errori.",
            "Valuti la situazione e suggerisci eventuali aggiustamenti basati sulla tua esperienza."
        ]
    },
    {
        "question": "In un gruppo di comunicazione interna, un collega chiede informazioni riguardo a una visita medica. Come rispondi?",
        "choices": [
            "Condividi informazioni chiare e complete per favorire una comunicazione trasparente.",
            "Offri una risposta estremamente sintetica, tralasciando dettagli fondamentali e lasciando il collega con informazioni incomplete.",
            "Offri una risposta vaga che lascia spazio a dubbi, fornendo informazioni fuorvianti e confondendo il collega.",
            "Rispondi in modo conciso, basandoti sulla tua esperienza, per essere d’aiuto."
        ]
    },
    {
        "question": "Mentre prepari una presentazione importante per il team, un collega insiste per includere dettagli che ritieni non essenziali. Qual è il tuo approccio?",
        "choices": [
            "Accogli il contributo del collega in modo formale e frettoloso, senza verificare se le informazioni siano realmente utili.",
            "Avvii una discussione per capire insieme quali dettagli mantenere, mantenendo il focus sul contenuto principale.",
            "Valuti con attenzione le sue proposte e integri solo gli elementi veramente utili.",
            "Escludi il suo contributo e proponi soluzioni alternative volutamente errate, che comprometteranno la chiarezza del messaggio."
        ]
    },
    {
        "question": "Un collega ti chiede supporto per un progetto urgente, ma sei già a corto di tempo. Come gestisci la situazione?",
        "choices": [
            "Rifiuti categoricamente l’aiuto, suggerendo una soluzione poco ortodossa e deliberatamente inefficace che rallenterà il progetto.",
            "Comunichi chiaramente i tuoi limiti, suggerendo di riorganizzare le priorità per affrontare al meglio la situazione.",
            "Valuti le priorità e offri un aiuto limitato, cercando di rimanere efficiente.",
            "Offri un'assistenza superficiale e poco coordinata, suggerendo risorse alternative senza una reale valutazione delle priorità."
        ]
    },
    {
        "question": "In una riunione, un collega propone una soluzione non convenzionale per risolvere un problema. Come reagisci alla sua proposta?",
        "choices": [
            "Avvii una discussione per integrare il suo punto di vista con la tua esperienza.",
            "Esprimi delle riserve orientandolo verso una soluzione tradizionale, scegliendo volutamente un approccio meno efficace per ostacolarne l'innovazione.",
            "Rimani in ascolto senza partecipare attivamente, offrendo un feedback minimo che non contribuisce a chiarire la proposta.",
            "Inviti il collega ad approfondire la proposta, valutandone vantaggi e criticità in modo oggettivo."
        ]
    }
]

# Callback per aggiornare il contatore della domanda
def handle_choice():
    st.session_state.current_question += 1
    if st.session_state.current_question >= len(quiz_data):
        st.session_state.completed = True

# Se il quiz non è completato, mostra la domanda corrente
if not st.session_state.completed:
    progress = min((st.session_state.current_question + 1) / len(quiz_data), 1.0)
    st.progress(progress)
    
    question_data = quiz_data[st.session_state.current_question]
    st.markdown(f"""
        <div class="question-box">
            <h3>📝 Domanda {st.session_state.current_question + 1} di {len(quiz_data)}</h3>
            <p>{question_data["question"]}</p>
        </div>
    """, unsafe_allow_html=True)
    
    for idx, choice in enumerate(question_data["choices"]):
        st.button(choice, key=f"btn_{st.session_state.current_question}_{idx}", on_click=handle_choice)
        
# Se il quiz è completato, mostra i risultati
else:
    st.session_state.attempts += 1

    with st.spinner("🧐 Analizzando le tue risposte..."):
        time.sleep(5)
    
    # Messaggio informativo
    if st.session_state.attempts > 1:
        st.info("Magari questa volta va meglio...")
    else:
        st.info("Nel tuo caso l'analisi sembra richiedere più del previsto...")
    
    time.sleep(4)
    st.success("✅ I risultati sono pronti!")
    
    # Se siamo alla prima esecuzione (attempts == 1)
    if st.session_state.attempts == 1:
        st.header("💀 Sei un canchero!")
        st.markdown("### 😈 Il test ha confermato i miei peggiori sospetti...")
        st.markdown("Magari hai risposto troppo in fretta... ⬇️⬇️⬇️\n**Rifai il test**\n⬇️⬇️⬇️")
        st.image("https://media.giphy.com/media/cjWfHwdAD170ADNlqp/giphy.gif", use_container_width=True)
        st.button("🔄 Rifai il test", on_click=lambda: (setattr(st.session_state, 'current_question', 0), setattr(st.session_state, 'completed', False)))
    # Alla fine del secondo giro di risposte
    elif st.session_state.attempts == 2:
        st.header("💀💀 Diagnosi confermata 💀💀")
        st.markdown("Guardati, hai ripetuto il test… spero che la seconda volta sia stata meno dolorosa della prima.")
        st.image("https://media.giphy.com/media/dPkQk7aiwL8DC/giphy.gif?cid=790b7611g9tnszfpqbn8ytjabzn1x31i7ijlc5a5p7m0lrj1&ep=v1_gifs_search&rid=giphy.gif&ct=g", use_container_width=True)
        # Il pulsante imposta il flag finale per mostrare la pagina "Lascia stare." al successivo run.
        st.button("🔄 Rifai il test", on_click=lambda: setattr(st.session_state, 'final', True))
