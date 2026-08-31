"""Tema visual para la app Streamlit de gestión de alquileres.

Importar este módulo no cambia datos ni lógica de negocio. La función pública
debe ejecutarse antes del primer elemento visual de Streamlit.
"""

import streamlit as st


def preparar_cromo_profesional(codigo: str) -> str:
    """Retira emojis decorativos, sin alterar los avisos y estados funcionales."""
    reemplazos = {
        '"🚜 Gestión de Alquiler de Máquinas"': '"Gestión de Alquiler de Máquinas"',
        '"👥 Clientes"': '"Clientes"',
        '"🛠️ Máquinas"': '"Máquinas"',
        '"📋 Alquileres y Devoluciones"': '"Alquileres y Devoluciones"',
        '"💰 Ingresos (Privado)"': '"Ingresos (Privado)"',
        '"📝 Registrar Nuevo Cliente"': '"Registrar Nuevo Cliente"',
        '"🔍 Buscador y Gestión de Clientes"': '"Buscador y Gestión de Clientes"',
        '"🛠️ Catálogo de Máquinas"': '"Catálogo de Máquinas"',
        '"📦 Inventario"': '"Inventario"',
        '"✏️ Editar tarifas de una máquina"': '"Editar tarifas de una máquina"',
        '"➕ Agregar una máquina adicional"': '"Agregar una máquina adicional"',
        '"➕ Registrar nuevo alquiler"': '"Registrar nuevo alquiler"',
        '"🛒 Máquinas Seleccionadas"': '"Máquinas seleccionadas"',
        '"💰 Resumen y pago"': '"Resumen y pago"',
        '"🔄 Alquileres actualmente en la calle"': '"Alquileres actualmente en la calle"',
        '"💰 Resumen de Ingresos del Local"': '"Resumen de ingresos del local"',
        '"📈 Totales Acumulados"': '"Totales acumulados"',
        '"🔍 Historial Detallado por Cuenta"': '"Historial detallado por cuenta"',
    }
    for original, reemplazo in reemplazos.items():
        codigo = codigo.replace(original, reemplazo)
    return codigo


def aplicar_estilo_gestion() -> None:
    """Configura una interfaz operativa, legible y consistente para el local."""
    st.set_page_config(
        page_title="Gestión de Alquiler de Máquinas",
        page_icon="🚜",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.markdown(
        """
        <style>
        :root {
            --ink: #17221c;
            --ink-soft: #526057;
            --surface: #ffffff;
            --surface-muted: #f0f3ee;
            --canvas: #f5f6f3;
            --line: #dce2da;
            --line-strong: #c6d0c5;
            --accent: #ae7421;
            --accent-strong: #805216;
            --success: #1f7652;
            --warning: #9a5b00;
            --danger: #b43632;
            --focus: #155fc1;
            --radius: 16px;
            --radius-control: 11px;
            --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
            --ease-press: cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        .stApp {
            background: var(--canvas);
            color: var(--ink);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI Variable", "Segoe UI", sans-serif;
            font-variant-numeric: proportional-nums;
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }

        .stApp::before {
            content: "";
            position: fixed;
            inset: 0 0 auto;
            z-index: 0;
            height: 3px;
            background: var(--accent);
            pointer-events: none;
        }

        .main .block-container {
            position: relative;
            z-index: 1;
            max-width: 1360px;
            padding: 1.85rem clamp(1rem, 3vw, 3rem) 4.75rem;
        }

        h1, h2, h3, [data-testid="stMarkdownContainer"] h1,
        [data-testid="stMarkdownContainer"] h2,
        [data-testid="stMarkdownContainer"] h3 {
            color: var(--ink);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI Variable", "Segoe UI", sans-serif;
            font-optical-sizing: auto;
            text-wrap: balance;
        }

        h1, [data-testid="stMarkdownContainer"] h1 {
            display: none;
        }

        .premium-identity {
            display: flex;
            align-items: end;
            justify-content: space-between;
            gap: 2rem;
            margin: 0 0 1.15rem;
            padding: 0.45rem 0 1.45rem;
            border-bottom: 1px solid var(--line);
        }

        .premium-identity__title {
            margin: 0;
            color: var(--ink);
            font-size: clamp(2.25rem, 4vw, 4.35rem) !important;
            font-weight: 700 !important;
            letter-spacing: -0.04em !important;
            line-height: 0.98 !important;
            text-wrap: balance;
        }

        .premium-identity__context {
            max-width: 25rem;
            margin: 0 0 0.18rem;
            color: var(--ink-soft);
            font-size: 0.93rem !important;
            font-weight: 500 !important;
            line-height: 1.5 !important;
            text-align: right;
        }

        h2, [data-testid="stMarkdownContainer"] h2 {
            margin-top: 2.6rem;
            font-size: clamp(1.3rem, 1.8vw, 1.7rem);
            font-weight: 680;
            letter-spacing: -0.025em;
            line-height: 1.18;
        }

        h3, [data-testid="stMarkdownContainer"] h3 {
            margin-top: 1.35rem;
            font-size: 1.1rem;
            font-weight: 650;
            letter-spacing: -0.012em;
            line-height: 1.3;
        }

        p, label, [data-testid="stCaptionContainer"] {
            color: var(--ink-soft);
            font-variant-numeric: proportional-nums;
        }

        [data-testid="stCaptionContainer"] {
            font-size: 0.82rem;
            line-height: 1.45;
        }

        hr {
            margin: 2.6rem 0;
            border: 0;
            border-top: 1px solid var(--line);
        }

        /* Navegación principal */
        [data-baseweb="tab-list"] {
            gap: 0.4rem;
            margin-bottom: 1.3rem;
            padding: 0.35rem;
            border-bottom: 0;
            border-radius: 12px;
            background: #e3e7e1;
        }

        [data-baseweb="tab"] {
            height: 2.55rem;
            padding: 0 0.9rem;
            border-radius: 9px;
            color: var(--ink-soft);
            font-size: 0.9rem;
            font-weight: 650;
            transition: background-color 160ms var(--ease-out), color 160ms var(--ease-out), transform 120ms var(--ease-out);
        }

        [data-baseweb="tab"]:hover {
            color: var(--ink);
            background: rgba(255, 255, 255, 0.6);
        }

        [data-baseweb="tab"][aria-selected="true"] {
            color: #fff;
            background: var(--ink);
        }

        [data-baseweb="tab-highlight"] { display: none; }

        /* API de tabs de Streamlit actual */
        [data-testid="stTabs"] [role="tablist"] {
            display: flex;
            gap: 0.4rem;
            margin-bottom: 1.3rem;
            padding: 0.32rem;
            border: 1px solid rgba(255, 255, 255, 0.62) !important;
            border-radius: 14px;
            background: rgba(229, 234, 228, 0.76);
            backdrop-filter: saturate(155%) blur(18px);
            -webkit-backdrop-filter: saturate(155%) blur(18px);
        }

        [data-testid="stTab"] {
            min-height: 2.5rem;
            padding: 0 0.95rem;
            border: 1px solid transparent !important;
            border-radius: 10px;
            color: var(--ink-soft);
            font-size: 0.86rem;
            font-weight: 650;
            letter-spacing: -0.006em;
            transition: background-color 160ms var(--ease-out), color 160ms var(--ease-out), box-shadow 180ms var(--ease-out);
        }

        [data-testid="stTab"][aria-selected="true"] {
            background: var(--ink);
            color: #ffffff;
            box-shadow: 0 3px 10px rgba(23, 34, 28, 0.16);
        }

        [data-testid="stTab"]:focus-visible {
            outline: 3px solid rgba(21, 95, 193, 0.3) !important;
            outline-offset: 2px;
        }

        /* Contenedores de información y formularios */
        [data-testid="stVerticalBlockBorderWrapper"] {
            border: 1px solid var(--line);
            border-radius: var(--radius);
            background: var(--surface);
        }

        [data-testid="stVerticalBlockBorderWrapper"] > div {
            padding: clamp(0.9rem, 1.8vw, 1.35rem);
        }

        [data-testid="stForm"] {
            margin-top: 0.55rem;
            padding: clamp(1.1rem, 2vw, 1.65rem);
            border: 0;
            border-radius: var(--radius);
            background: var(--surface);
            box-shadow: 0 16px 36px rgba(23, 34, 28, 0.075);
        }

        [data-testid="stMetric"] {
            min-height: 5.8rem;
            padding: 0.8rem 0.2rem;
            border: 0;
            border-radius: 0;
            background: transparent;
        }

        [data-testid="stMetricLabel"] {
            color: var(--ink-soft);
            font-size: 0.78rem;
            font-weight: 650;
            letter-spacing: 0.012em;
        }

        [data-testid="stMetricValue"] {
            color: var(--ink);
            font-variant-numeric: tabular-nums;
            font-size: 1.48rem;
            font-weight: 700;
            letter-spacing: -0.03em;
        }

        /* Campos */
        label[data-testid="stWidgetLabel"] p {
            color: var(--ink);
            font-size: 0.86rem;
            font-weight: 680;
        }

        [data-baseweb="input"] > div,
        [data-baseweb="select"] > div,
        [data-baseweb="textarea"] {
            min-height: 2.65rem;
            border-color: var(--line-strong) !important;
            border-radius: 10px !important;
            background: var(--surface) !important;
            box-shadow: none !important;
            transition: border-color 160ms var(--ease-out), box-shadow 160ms var(--ease-out), background-color 160ms var(--ease-out);
        }

        [data-baseweb="input"] > div:hover,
        [data-baseweb="select"] > div:hover,
        [data-baseweb="textarea"]:hover {
            border-color: #98a398 !important;
        }

        [data-baseweb="input"] > div:focus-within,
        [data-baseweb="select"] > div:focus-within,
        [data-baseweb="textarea"]:focus-within {
            border-color: var(--focus) !important;
            box-shadow: 0 0 0 3px rgba(23, 92, 211, 0.16) !important;
        }

        input, textarea {
            color: var(--ink) !important;
            font-variant-numeric: tabular-nums;
        }

        input::placeholder, textarea::placeholder { color: #78837b !important; }

        [data-baseweb="select"] * { color: var(--ink); }

        /* Streamlit 1.40+ usa componentes React Aria en lugar de BaseWeb.
           Esta capa mantiene cada campo inequívocamente blanco y legible. */
        [data-testid="stTextInputRootElement"],
        [data-testid="stNumberInputContainer"],
        [data-testid="stTextArea"] [data-testid$="RootElement"],
        [data-testid="stDateInput"] [data-testid$="RootElement"],
        [data-testid="stSelectbox"] .react-aria-ComboBox > div {
            min-height: 2.7rem;
            border: 1px solid var(--line-strong) !important;
            border-radius: var(--radius-control) !important;
            background: #ffffff !important;
            box-shadow: none !important;
            transition: transform 180ms var(--ease-out), border-color 160ms var(--ease-out), box-shadow 160ms var(--ease-out);
        }

        [data-testid="stTextInputField"],
        [data-testid="stNumberInputField"],
        [data-testid="stTextArea"] textarea,
        [data-testid="stDateInput"] input,
        [data-testid="stSelectbox"] input {
            background: transparent !important;
            color: var(--ink) !important;
            caret-color: var(--ink);
        }

        [data-testid="stTextInputField"]::placeholder,
        [data-testid="stNumberInputField"]::placeholder,
        [data-testid="stTextArea"] textarea::placeholder,
        [data-testid="stDateInput"] input::placeholder,
        [data-testid="stSelectbox"] input::placeholder {
            color: #647168 !important;
            opacity: 1;
        }

        [data-testid="stTextInputRootElement"]:focus-within,
        [data-testid="stNumberInputContainer"]:focus-within,
        [data-testid="stTextArea"] [data-testid$="RootElement"]:focus-within,
        [data-testid="stDateInput"] [data-testid$="RootElement"]:focus-within,
        [data-testid="stSelectbox"] .react-aria-ComboBox > div:focus-within {
            border-color: var(--focus) !important;
            box-shadow: 0 0 0 3px rgba(21, 95, 193, 0.15) !important;
        }

        [data-testid="stNumberInputStepDown"],
        [data-testid="stNumberInputStepUp"] {
            border-color: transparent !important;
            background: #f1f4ef !important;
            color: var(--ink) !important;
        }

        [role="listbox"] {
            border: 0 !important;
            border-radius: 14px !important;
            background: #ffffff !important;
            box-shadow: 0 18px 42px rgba(23, 34, 28, 0.14) !important;
        }

        [role="option"] {
            color: var(--ink) !important;
            background: #ffffff !important;
        }

        [role="option"][data-focused="true"],
        [role="option"]:hover {
            background: #f1f4ef !important;
        }

        /* Acciones */
        .stButton > button,
        .stDownloadButton > button,
        .stFormSubmitButton > button {
            min-height: 2.65rem;
            padding: 0.5rem 1.05rem;
            border: 1px solid var(--line-strong);
            border-radius: var(--radius-control);
            background: var(--surface);
            color: var(--ink);
            font-size: 0.88rem;
            font-weight: 650;
            transition: background-color 160ms var(--ease-out), border-color 160ms var(--ease-out), color 160ms var(--ease-out), transform 140ms var(--ease-press), box-shadow 160ms var(--ease-out);
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover,
        .stFormSubmitButton > button:hover {
            border-color: var(--ink);
            background: #f4f6f2;
        }

        .stButton > button[kind="primary"],
        .stFormSubmitButton > button[kind="primary"] {
            border-color: var(--ink);
            background: var(--ink);
            color: #fff;
        }

        .stButton > button[kind="primary"]:hover,
        .stFormSubmitButton > button[kind="primary"]:hover {
            border-color: #2c3932;
            background: #2c3932;
            box-shadow: 0 8px 18px rgba(23, 34, 28, 0.16);
        }

        .stButton > button:active,
        .stDownloadButton > button:active,
        .stFormSubmitButton > button:active,
        [data-baseweb="tab"]:active {
            transform: scale(0.97);
            transition-duration: 100ms;
        }

        button:disabled {
            border-color: var(--line) !important;
            background: #e9ece8 !important;
            color: #89938c !important;
            opacity: 1 !important;
        }

        button:focus-visible,
        a:focus-visible,
        [data-baseweb="tab"]:focus-visible {
            outline: 3px solid rgba(23, 92, 211, 0.32) !important;
            outline-offset: 2px;
        }

        /* Listados, avisos y desplegables */
        [data-testid="stDataFrame"], [data-testid="stDataEditor"] {
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: 14px;
            background: var(--surface);
            font-variant-numeric: tabular-nums;
        }

        [data-testid="stAlert"] {
            border: 1px solid var(--line);
            border-radius: 12px;
            background: var(--surface-muted);
            color: var(--ink);
        }

        [data-testid="stExpander"] {
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: 14px;
            background: var(--surface);
        }

        [data-testid="stExpander"] summary {
            padding: 0.2rem 0.25rem;
            color: var(--ink);
            font-weight: 650;
        }

        [data-testid="stFileUploader"] {
            border-radius: 12px;
        }

        [data-testid="stFileUploaderDropzone"] {
            border: 1px dashed #aeb8ae;
            border-radius: 14px;
            background: #ffffff;
        }

        [data-testid="stFileUploader"] button {
            border-color: var(--ink) !important;
            background: var(--ink) !important;
            color: #ffffff !important;
        }

        [data-testid="stFileUploader"] button p {
            color: #ffffff !important;
        }

        [data-testid="stFileUploaderDropzone"] > div > span {
            color: var(--ink-soft) !important;
        }

        [data-testid="stFileUploader"] button:hover {
            border-color: #2c3932 !important;
            background: #2c3932 !important;
            color: #ffffff !important;
        }

        /* Superficies del navegador */
        ::selection { background: #efd296; color: #17221c; }

        ::-webkit-scrollbar { width: 11px; height: 11px; }
        ::-webkit-scrollbar-track { background: #eaede8; }
        ::-webkit-scrollbar-thumb {
            border: 3px solid #eaede8;
            border-radius: 99px;
            background: #849087;
        }
        ::-webkit-scrollbar-thumb:hover { background: #5d685f; }

        @media (hover: hover) and (pointer: fine) {
            [data-testid="stVerticalBlockBorderWrapper"] {
                transition: border-color 160ms var(--ease-out);
            }
            [data-testid="stVerticalBlockBorderWrapper"]:hover {
                border-color: #b7c0b7;
            }

            [data-testid="stTextInputRootElement"]:hover,
            [data-testid="stNumberInputContainer"]:hover,
            [data-testid="stTextArea"] [data-testid$="RootElement"]:hover,
            [data-testid="stDateInput"] [data-testid$="RootElement"]:hover,
            [data-testid="stSelectbox"] .react-aria-ComboBox > div:hover {
                border-color: #98a398 !important;
                transform: translateY(-1px);
                will-change: transform;
            }

            .stButton > button:hover,
            .stDownloadButton > button:hover,
            .stFormSubmitButton > button:hover {
                transform: translateY(-1px);
                will-change: transform;
            }
        }

        @media (max-width: 760px) {
            .main .block-container {
                padding-top: 1.35rem;
                padding-inline: 1rem;
            }

            .premium-identity {
                display: block;
                margin-bottom: 1rem;
                padding-bottom: 1.15rem;
            }

            .premium-identity__title {
                font-size: clamp(2.35rem, 11vw, 3.25rem) !important;
            }

            .premium-identity__context {
                margin-top: 0.85rem;
                text-align: left;
            }

            [data-baseweb="tab-list"],
            [data-testid="stTabs"] [role="tablist"] {
                gap: 0.25rem;
                overflow-x: auto;
                padding: 0.25rem;
                scrollbar-width: none;
            }

            [data-baseweb="tab-list"]::-webkit-scrollbar,
            [data-testid="stTabs"] [role="tablist"]::-webkit-scrollbar {
                display: none;
            }

            [data-baseweb="tab"],
            [data-testid="stTab"] {
                flex: 0 0 auto;
                padding-inline: 0.75rem;
                font-size: 0.82rem;
            }

            [data-testid="stMetric"] { min-height: 5.6rem; }
        }

        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                scroll-behavior: auto !important;
                transition-duration: 0.01ms !important;
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
            }

            [data-testid="stTextInputRootElement"]:hover,
            [data-testid="stNumberInputContainer"]:hover,
            [data-testid="stTextArea"] [data-testid$="RootElement"]:hover,
            [data-testid="stDateInput"] [data-testid$="RootElement"]:hover,
            [data-testid="stSelectbox"] .react-aria-ComboBox > div:hover,
            .stButton > button:hover,
            .stDownloadButton > button:hover,
            .stFormSubmitButton > button:hover {
                transform: none;
            }
        }

        @media (prefers-reduced-transparency: reduce) {
            [data-testid="stTabs"] [role="tablist"] {
                background: #e3e7e1;
                backdrop-filter: none;
                -webkit-backdrop-filter: none;
            }
        }

        @media (prefers-contrast: more) {
            [data-testid="stTextInputRootElement"],
            [data-testid="stNumberInputContainer"],
            [data-testid="stTextArea"] [data-testid$="RootElement"],
            [data-testid="stDateInput"] [data-testid$="RootElement"],
            [data-testid="stSelectbox"] .react-aria-ComboBox > div,
            .stButton > button,
            .stDownloadButton > button,
            .stFormSubmitButton > button {
                border-color: #17221c !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <header class="premium-identity" aria-label="Gestión de alquileres">
            <p class="premium-identity__title">Gestión de alquileres</p>
            <p class="premium-identity__context">
                Clientes, máquinas, alquileres e ingresos en una única operación.
            </p>
        </header>
        """,
        unsafe_allow_html=True,
    )
