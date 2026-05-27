// Shared bilingual content for LA REAL
// Loads as a plain script — exposes window.CONTENT

window.CONTENT = {
  brand: { name: 'LA REAL', tagline_es: 'Growth Partners', tagline_en: 'Growth Partners' },

  nav: {
    es: ['Servicios', 'Resultados', 'Clientes', 'Nosotros', 'Contacto'],
    en: ['Services', 'Results', 'Clients', 'About', 'Contact'],
  },

  hero: {
    eyebrow: { es: 'Growth Partners para e-commerce', en: 'Growth Partners for e-commerce' },
    title: {
      es: ['Hacemos crecer', 'las marcas', 'que ya están listas', 'para escalar.'],
      en: ['We scale the brands', 'that are ready', 'to grow', 'online.'],
    },
    sub: {
      es: 'Con estrategias comprobadas en +150 marcas a nivel mundial.',
      en: 'With strategies proven across +150 brands worldwide.',
    },
    cta_primary: { es: 'Aplica con tu marca', en: 'Apply with your brand' },
    cta_secondary: { es: 'Ver casos', en: 'See case studies' },
  },

  manifesto: {
    es: 'No vendemos humo. Vendemos crecimiento medible.',
    en: "We don't sell smoke. We sell measurable growth.",
  },

  // Services toggle: Growth Partners ↔ Growth Advisor
  services: {
    partners: {
      key: 'partners',
      tab_label: { es: 'Growth Partners', en: 'Growth Partners' },
      tagline: {
        es: 'Para marcas que ya venden y quieren escalar.',
        en: 'For brands already selling, ready to scale.',
      },
      desc: {
        es: 'Entramos como tu socio de crecimiento. Operamos el embudo end-to-end con la rigurosidad de un CFO y la creatividad de un estudio.',
        en: 'We join you as your growth partner. We run the funnel end-to-end with the discipline of a CFO and the craft of a studio.',
      },
      cta: {
        es: { line1: 'Aplicar a Growth Partner', line2: 'Tengo una marca que ya vende y quiero escalar' },
        en: { line1: 'Apply to Growth Partner', line2: 'My brand already sells and I want to scale' },
      },
      pillars: [
        { id: '01', es: { t: 'Estrategia 360º del embudo', d: 'Awareness, consideración, conversión y retención. Una sola hoja de ruta.' }, en: { t: '360º Funnel strategy', d: 'Awareness, consideration, conversion, retention. One single roadmap.' } },
        { id: '02', es: { t: 'Paid Media', d: 'Meta, Google, TikTok. Estructura de cuenta, creativos y bidding pensados para escalar.' }, en: { t: 'Paid Media', d: 'Meta, Google, TikTok. Account structure, creative and bidding built to scale.' } },
        { id: '03', es: { t: 'Email & Retention', d: 'Flujos, segmentación y campañas. El canal que multiplica el LTV.' }, en: { t: 'Email & Retention', d: 'Flows, segmentation, campaigns. The channel that multiplies LTV.' } },
        { id: '04', es: { t: 'Contenido', d: 'Creativos UGC, performance creative y branded content que convierte.' }, en: { t: 'Content', d: 'UGC, performance creative and branded content that converts.' } },
      ],
    },
    advisor: {
      key: 'advisor',
      tab_label: { es: 'Growth Advisor', en: 'Growth Advisor' },
      tagline: {
        es: 'Para marcas que están despegando en digital.',
        en: 'For brands taking off in digital.',
      },
      desc: {
        es: 'Sesiones uno a uno. Te enseñamos exactamente qué hacer para que tu marca empiece a vender y crecer en internet.',
        en: 'One-on-one sessions. We teach you exactly what to do so your brand starts selling and growing online.',
      },
      cta: {
        es: { line1: 'Aplicar a Growth Advisor', line2: 'Tengo una marca y quiero consultoría para aprender a tener mis primeras ventas' },
        en: { line1: 'Apply to Growth Advisor', line2: 'I have a brand and I want coaching to get my first sales' },
      },
      pillars: [
        { id: '01', es: { t: 'Diagnóstico inicial', d: 'Auditoría 360º de tu marca, oferta, canales y métricas actuales.' }, en: { t: 'Diagnosis', d: 'Full audit of your brand, offer, channels and current metrics.' } },
        { id: '02', es: { t: 'Sesiones 1:1', d: 'Trabajamos contigo en vivo. Te enseñamos el cómo, no solo el qué.' }, en: { t: '1:1 Sessions', d: 'We work live with you. We teach you the how, not just the what.' } },
        { id: '03', es: { t: 'Plan de acción', d: 'Roadmap claro y priorizado por impacto. Saber por dónde empezar.' }, en: { t: 'Action plan', d: 'A clear roadmap prioritised by impact. Know where to start.' } },
        { id: '04', es: { t: 'Acompañamiento', d: 'Resolvemos dudas, revisamos avances y ajustamos la ruta cada semana.' }, en: { t: 'Coaching', d: 'We answer questions, review progress and adjust weekly.' } },
      ],
    },
  },

  results: {
    title: { es: 'Resultados que se miden.', en: 'Results that get measured.' },
    sub: { es: 'Cifras agregadas de marcas que escalamos en los últimos 24 meses.', en: 'Aggregate numbers from brands we scaled in the last 24 months.' },
    stats: [
      { value: 4.2, suffix: 'x', label: { es: 'ROAS promedio sostenido', en: 'Sustained avg. ROAS' } },
      { value: 180, suffix: '%', prefix: '+', label: { es: 'Crecimiento en revenue email', en: 'Email revenue growth' } },
      { value: 60, suffix: '+', label: { es: 'Marcas escaladas', en: 'Brands scaled' } },
      { value: '+$2,000M', label: { es: 'Gestionados en paid media', en: 'Managed in paid media' } },
    ],
  },

  clients: {
    title: { es: 'Marcas que confían en nosotros.', en: 'Brands that trust us.' },
    list: ['Barba Roja','Leonisa','Parchita','Once','Pachha','Zorro y Jaguar','Estruendo','Ukelele','Sandra Botero','Yo vivo en gratitud','Cíclico','IFW','Adriza','Dulcey','Kryolan','Atratus'],
  },

  testimonials: {
    title: { es: 'Lo que dicen nuestros socios.', en: 'What our partners say.' },
    items: [
      {
        quote: {
          es: 'Trabajar con La Real ha sido una experiencia muy positiva para nosotros. Pasamos de tener un canal digital con poca relevancia a convertirlo en uno de los principales generadores de ventas de nuestra marca. Gracias a su acompañamiento, logramos estructurar mejor nuestro equipo y optimizar la pauta digital, lo que ha impulsado un crecimiento exponencial en las ventas de nuestra página web.',
          en: 'Working with La Real has been a hugely positive experience for us. We went from having a digital channel with little relevance to making it one of our brand\u2019s main revenue drivers. Thanks to their support we restructured our team and optimised paid media, which has driven exponential growth in our online sales.',
        },
        author: 'Miguel',
        role: { es: 'Cíclico', en: 'Cíclico' },
      },
      {
        quote: {
          es: 'Desde Barba Roja encontramos en La Real un aliado estratégico de verdad. Más que una agencia, han sido un equipo comprometido que entiende nuestra marca, nos reta constantemente y nos acompaña en cada decisión clave. Gracias a su enfoque claro y su lectura del mercado, logramos estructurar campañas que conectan con nuestra audiencia y generan resultados reales. Ha sido una experiencia de crecimiento, orden y proyección.',
          en: 'At Barba Roja we\u2019ve found a true strategic ally in La Real. More than an agency, they\u2019ve been a committed team that understands our brand, challenges us constantly and walks with us through every key decision. Thanks to their clear focus and read of the market we structured campaigns that connect with our audience and generate real results. It\u2019s been an experience of growth, order and projection.',
        },
        author: 'Santiago',
        role: { es: 'Barba Roja', en: 'Barba Roja' },
      },
    ],
  },

  about: {
    title: { es: 'Sobre LA REAL.', en: 'About LA REAL.' },
    paragraphs: {
      es: [
        'Somos un equipo de personas con +5 años de experiencia cada una ayudando marcas de e-commerce a lograr sus objetivos más ambiciosos.',
        'Trabajamos con un manifiesto simple: si tu marca no crece, nosotros tampoco. Por eso somos socios, no proveedores.',
      ],
      en: [
        'We are a team of people, each with 5+ years of experience helping e-commerce brands reach their most ambitious goals.',
        "We work with a simple manifesto: if your brand doesn't grow, we don't either. That's why we are partners, not vendors.",
      ],
    },
    team: [
      { name: 'Juan Felipe León', role: { es: 'Co-founder · Estrategia & Comercial', en: 'Co-founder · Strategy & Sales' }, initials: 'JL', photo: 'assets/team/juanfe.jpg' },
      { name: 'Santiago Upegui', role: { es: 'Paid Media · Contenidos', en: 'Paid Media · Content' }, initials: 'SU', photo: 'assets/team/santiago.jpg' },
      { name: 'Nicolás Agudelo', role: { es: 'Paid Media · CRO', en: 'Paid Media · CRO' }, initials: 'NA', photo: 'assets/team/nicolas.jpg' },
      { name: 'Laura Martínez', role: { es: 'Líder de Contenidos', en: 'Content Lead' }, initials: 'LM', photo: 'assets/team/laura.jpg' },
    ],
  },

  // Modal de aplicación: mini-selector + 2 formularios calificadores + agendar
  apply: {
    // Mini-selector cuando dan clic a CTAs genéricos del nav/hero
    selector: {
      title: { es: '¿Cómo te ayudamos?', en: 'How can we help?' },
      sub: {
        es: 'Tenemos dos formas de trabajar juntos. Elige la que más se parezca a tu situación.',
        en: 'We have two ways of working together. Pick the one that fits you best.',
      },
      options: {
        partner: {
          tag: { es: 'Growth Partner', en: 'Growth Partner' },
          title: { es: 'Ya vendo online y quiero escalar.', en: 'I already sell online and want to scale.' },
          desc: {
            es: 'Mi marca factura, tengo pauta corriendo y necesito un socio que opere el embudo conmigo.',
            en: 'My brand is selling, I run paid media, and I need a partner to operate the funnel with me.',
          },
        },
        advisor: {
          tag: { es: 'Growth Advisor', en: 'Growth Advisor' },
          title: { es: 'Estoy arrancando o quiero aprender.', en: 'I’m just starting or want to learn.' },
          desc: {
            es: 'Tengo una marca pero todavía no he despegado en digital. Quiero consultoría 1:1 para aprender.',
            en: "I have a brand but I haven't taken off online yet. I want 1:1 coaching to learn.",
          },
        },
      },
    },

    // Etiquetas comunes
    common: {
      back: { es: '← Volver', en: '← Back' },
      next: { es: 'Continuar →', en: 'Continue →' },
      submit_and_book: { es: 'Continuar a agendar →', en: 'Continue to book →' },
      required: { es: 'Requerido', en: 'Required' },
      step_form: { es: 'Paso 1 de 2 · Cuéntanos sobre tu marca', en: 'Step 1 of 2 · Tell us about your brand' },
      step_calendar: { es: 'Paso 2 de 2 · Agenda tu llamada', en: 'Step 2 of 2 · Book your call' },
      booking: { es: 'Agendando…', en: 'Booking…' },
      submitted_title: { es: '✓ Llamada agendada', en: '✓ Call booked' },
      submitted_sub: {
        es: 'Te enviamos un correo con todos los detalles y el link de Google Meet.',
        en: "We've sent you an email with all the details and the Google Meet link.",
      },
      submitted_close: { es: 'Cerrar', en: 'Close' },
      error_title: { es: 'Algo salió mal', en: 'Something went wrong' },
      error_sub: {
        es: 'No pudimos agendar tu llamada. Inténtalo de nuevo o escríbenos a hola@lareal.co.',
        en: "We couldn't book your call. Please try again or email hola@lareal.co.",
      },
      error_retry: { es: 'Reintentar', en: 'Try again' },
    },

    // Formulario A — Growth Partner (marca que ya vende)
    partner: {
      title: { es: 'Aplica como Growth Partner.', en: 'Apply as a Growth Partner.' },
      sub: {
        es: 'Estos datos nos ayudan a entender el tamaño y la madurez de tu marca antes de la llamada.',
        en: 'These details help us understand the size and maturity of your brand before the call.',
      },
      fields: {
        name: { label: { es: 'Tu nombre', en: 'Your name' }, ph: { es: 'María Pérez', en: 'Maria Perez' } },
        email: { label: { es: 'Email corporativo', en: 'Work email' }, ph: { es: 'maria@tumarca.co', en: 'maria@yourbrand.com' } },
        phone: { label: { es: 'Teléfono / WhatsApp', en: 'Phone / WhatsApp' }, ph: { es: '+57 300 000 0000', en: '+1 555 000 0000' } },
        brand: { label: { es: 'Marca', en: 'Brand name' }, ph: { es: 'Tu marca', en: 'Your brand' } },
        website: { label: { es: 'URL del sitio', en: 'Website URL' }, ph: { es: 'https://tumarca.co', en: 'https://yourbrand.com' } },
        category: {
          label: { es: 'Categoría', en: 'Category' },
          options: {
            es: ['Selecciona…', 'Moda y accesorios', 'Belleza y cuidado personal', 'Alimentos y bebidas', 'Hogar y decoración', 'Wellness y suplementos', 'Tech y gadgets', 'Otro'],
            en: ['Select…', 'Fashion & accessories', 'Beauty & personal care', 'Food & beverage', 'Home & decor', 'Wellness & supplements', 'Tech & gadgets', 'Other'],
          },
        },
        time_selling: {
          label: { es: '¿Hace cuánto vendes online?', en: 'How long have you been selling online?' },
          options: {
            es: ['Selecciona…', 'Menos de 6 meses', '6 a 12 meses', '1 a 2 años', 'Más de 2 años'],
            en: ['Select…', 'Less than 6 months', '6 to 12 months', '1 to 2 years', 'More than 2 years'],
          },
        },
        revenue: {
          label: { es: 'Facturación mensual actual', en: 'Current monthly revenue' },
          options: {
            es: ['Selecciona…', '$15M – $30M COP', '$30M – $100M COP', '$100M – $300M COP', '$300M – $1.000M COP', '+$1.000M COP'],
            en: ['Select…', '$4K – $7.5K USD', '$7.5K – $25K USD', '$25K – $75K USD', '$75K – $250K USD', '+$250K USD'],
          },
        },
        ad_spend: {
          label: { es: 'Inversión actual en pauta digital / mes', en: 'Current monthly ad spend' },
          options: {
            es: ['Selecciona…', 'No invierto aún', 'Menos de $5M COP', '$5M – $20M', '$20M – $50M', '$50M – $150M', '+$150M'],
            en: ['Select…', "I don't invest yet", 'Under $1.2K USD', '$1.2K – $5K', '$5K – $12K', '$12K – $35K', '+$35K'],
          },
        },
        has_agency: {
          label: { es: '¿Trabajas hoy con alguna agencia?', en: 'Do you work with an agency today?' },
          options: { es: ['Selecciona…', 'Sí', 'No'], en: ['Select…', 'Yes', 'No'] },
        },
        goal: {
          label: { es: '¿Cuál es tu objetivo en los próximos 12 meses?', en: 'What’s your goal for the next 12 months?' },
          ph: {
            es: 'Cuéntanos brevemente qué quieres lograr: facturación objetivo, lanzamientos, expansión, etc.',
            en: 'Briefly tell us your target revenue, launches, expansion plans, etc.',
          },
        },
      },
    },

    // Formulario B — Growth Advisor (marca arrancando)
    advisor: {
      title: { es: 'Aplica como Growth Advisor.', en: 'Apply as a Growth Advisor.' },
      sub: {
        es: 'Cuéntanos en qué etapa estás. La llamada es para entender qué necesitas aprender y resolver.',
        en: 'Tell us your stage. The call is to understand what you need to learn and solve.',
      },
      fields: {
        name: { label: { es: 'Tu nombre', en: 'Your name' }, ph: { es: 'María Pérez', en: 'Maria Perez' } },
        email: { label: { es: 'Email', en: 'Email' }, ph: { es: 'maria@correo.com', en: 'maria@email.com' } },
        phone: { label: { es: 'Teléfono / WhatsApp', en: 'Phone / WhatsApp' }, ph: { es: '+57 300 000 0000', en: '+1 555 000 0000' } },
        brand: { label: { es: 'Marca', en: 'Brand name' }, ph: { es: 'Tu marca', en: 'Your brand' } },
        website: { label: { es: 'URL o Instagram', en: 'Website or Instagram' }, ph: { es: '@tumarca · tumarca.co', en: '@yourbrand · yourbrand.com' } },
        stage: {
          label: { es: '¿En qué etapa estás?', en: 'What stage are you at?' },
          options: {
            es: ['Selecciona…', 'Pre-lanzamiento (todavía no vendo)', 'Lancé pero no vendo aún', 'Vendo poquito, sin estructura', 'Vendo regularmente, quiero estructura'],
            en: ['Select…', 'Pre-launch (not selling yet)', 'Launched but no sales yet', 'Selling a little, no structure', 'Selling regularly, want structure'],
          },
        },
        what_you_sell: {
          label: { es: '¿Qué vendes?', en: 'What do you sell?' },
          ph: { es: 'Cuéntanos en 1-2 líneas qué producto u oferta tienes.', en: 'Tell us in 1-2 lines what product or offer you have.' },
        },
        revenue: {
          label: { es: 'Facturación mensual aprox.', en: 'Approx. monthly revenue' },
          options: {
            es: ['Selecciona…', '$0 (aún no vendo)', 'Menos de $2M COP', '$2M – $10M', '$10M – $30M', '+$30M'],
            en: ['Select…', '$0 (not selling yet)', 'Under $500 USD', '$500 – $2.5K', '$2.5K – $7.5K', '+$7.5K'],
          },
        },
        tried: {
          label: { es: '¿Qué has probado hasta ahora?', en: 'What have you tried so far?' },
          ph: {
            es: 'Pauta, contenido, influencers, ferias… cuéntanos qué has hecho y qué resultados has tenido.',
            en: 'Ads, content, influencers, fairs… tell us what you’ve done and the results.',
          },
        },
        goal: {
          label: { es: '¿Qué te gustaría aprender o resolver?', en: 'What would you like to learn or solve?' },
          ph: {
            es: 'Por ejemplo: cómo armar mi primera campaña, cómo estructurar mi oferta, cómo medir resultados…',
            en: 'For example: how to set up my first campaign, how to structure my offer, how to measure results…',
          },
        },
      },
    },

    // Calendario (paso 2)
    calendar: {
      title: { es: 'Agenda tu llamada', en: 'Book your call' },
      sub: {
        es: 'Llamada de 30 minutos por Google Meet. Selecciona el día y la hora que te quede mejor.',
        en: '30-minute call on Google Meet. Pick the day and time that works best.',
      },
      pick_date: { es: 'Selecciona una fecha', en: 'Pick a date' },
      pick_time: { es: 'Selecciona una hora (hora Colombia)', en: 'Pick a time (Colombia time)' },
      no_slots: { es: 'No hay horas disponibles este día. Prueba otra fecha.', en: 'No slots available this day. Try another date.' },
      loading: { es: 'Cargando disponibilidad…', en: 'Loading availability…' },
      confirm: { es: 'Confirmar llamada', en: 'Confirm call' },
      timezone_note: { es: 'Horario en zona Colombia (UTC-5)', en: 'Time in Colombia (UTC-5)' },
    },
  },

  footer: {
    es: { addr: 'Medellín · Bogotá · Remote', tag: 'Growth Partners para e-commerce.', rights: '© 2026 LA REAL. Todos los derechos reservados.' },
    en: { addr: 'Medellín · Bogotá · Remote', tag: 'Growth Partners for e-commerce.', rights: '© 2026 LA REAL. All rights reserved.' },
  },
};
