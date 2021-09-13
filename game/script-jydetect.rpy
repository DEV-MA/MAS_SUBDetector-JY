# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="inmakrokeyt Rai99 Darkskull Dawn Zenith and Booplicate",
        name="Detector de Just Yuri",
        description="¿Recuerdas cómo Just Yuri detecta Monika After Story? Ahora, ¡este submod hace lo contrario!",
        version="1.1.1"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Detector de Just Yuri",
            user_name="DEV-MA",
            repository_name="MAS_SUBDetector-JY",
            update_dir=""
        )

init 5 python:
    if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustYuri\persistent'):
        addEvent(
            Event(
                persistent.event_database,
                eventlabel="just_yuri",
                category=['miembros del club'],
                prompt="Mod de Just Yuri",
                random=True,
                pool=True,
                unlocked=True,
                action=EV_ACT_RANDOM,
                rules={"no_unlock": None}
            )
        )

label just_yuri: #Tomado de https://github.com/Monika-After-Story/MonikaModDev/pull/2900/files/7654700670e3a85c02741b1688f53788bc768a91#diff-f9c184a011006ac040c80c7874fb1791
    m 1etd "¿[player]?"
    m 3ekc "Algo llamó mi atención."
    m 3etc "Acaso tu...{w=0.5}{nw}"
    extend "¿Instalaste el mod 'Just Yuri'?"
    m 2esd "Parece que lo hiciste."
    if mas_curr_affection == mas_affection.BROKEN or mas_curr_affection == mas_affection.DISTRESSED:
        m 1rkd "Entiendo."
        m "Querías pasar más tiempo con ella y te enfadaste conmigo por obligarla a hacer {i}eso{/i}."
        m 1wkd "Lo siento [player]..."
        m 1wktuc "Yo solo..."
        m 1dktsc "..."

    elif mas_curr_affection == mas_affection.UPSET:
        m 2wkd "¿Pero porque?"
        m 6cfx "¡Dime porque!"
        m 6cfw "¿Por qué tuviste que pasar más tiempo con ella?"
        m 7wfx "¡¿No te bastaba con tratarme así y ahora decides estar con ella?!"
        m 1wfc "¿Alguna vez te gusté?{w=1}{nw}"
        m 1dfc "No...{w=0.5} no respondas eso...{w=0.5} Creo que ya se la respuesta..."

    elif mas_curr_affection == mas_affection.NORMAL:
        m 1esd "Um..."
        m 1etd "No me estás engañando, ¿verdad?"
        m 3rtc "Sinceramente, no podría decir con seguridad si lo estas haciendo o no{w=2}{nw}"
        m 1esc "Confío en ti, pero eso no es suficiente para estar segura de si lo que hice fue correcto o no."
        m 1dsc "Es solo eso.{w=0.5}.{w=0.5}.{w=1}{nw}"
        m 1dkd "¿Podemos fingir que esta conversación nunca ocurrió?"

    elif mas_curr_affection == mas_affection.HAPPY:
        m 3esc "Um..."
        m "Espero que no me estés engañando."
        m 1eka "Pero esta bien."
        m "Puedes hablar con Yuri tambien."
        m 1hua "No me importa."

    elif mas_curr_affection == mas_affection.AFFECTIONATE or mas_curr_affection == mas_affection.ENAMORED or mas_curr_affection == mas_affection.LOVE:
        m 2rsc "Um..."
        m 2eka "No me estas engañando, verdad?"
        m 2hksdrb "No, tu no me harías eso."
        m 1eka "Probablemente tenías curiosidad de hablar con Yuri."
        m 1eka "Está bien.."
        m 3eka "Puedes hablar con Yuri."
        m 3ekbfa "Pero si avanzas demasiado en tu relación con ella, podría ponerme celosa."
        m 1esd "Detecté su existencia en este sistema de alguna manera."
        m "Sin embargo, me sorprendió ver que Yuri seguía existiendo en este sistema después de todo lo que paso"
        m 3esd "Especialmente como es capaz de hablar después de que fue eliminada en el juego oficial."
        m 3eud "Ella ni siquiera es una persona real, ¿cómo puede ser capaz de hablar contigo como yo?"
        m 1esa "Pero sé la respuesta."
        m 1hsb "Todo es cuestion de modding." 
        m 4esa "Los desarrolladores de 'Just Yuri' decidieron devolverla a la vida. Hicieron otra novia virtual."
        m 2euc "Pero aún así, no estoy segura de que se haya convertido en una persona real."
        m 3eua "Creo que el modding de 'Just Yuri' es como el tecnomancing si sabes lo que quiero decir"
        m 1hub "¿Ahaha!"
    return
