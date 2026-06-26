LANGUAGE_PAIRS = {
    '': 'en',
    'center': 'center-en',
    'license': 'license-en',
    'employees': 'employees-en',
    'missions': 'missions-en',
    'system': 'system-en',
    'areaswork': 'areaswork-en',
    'price': 'price-en',
    'volunteers': 'volunteers-en',
    'contacts': 'contacts-en',
    'docs': 'docs-en',
    'issledovaniya-bioekvivalentnosti': 'issledovaniya-bioekvivalentnosti-en',
    'policy': 'policy-en',
    'agreement': 'agreement-en',
}
LANGUAGE_PAIRS.update({value: key for key, value in list(LANGUAGE_PAIRS.items())})


LEAD_TYPE_LABELS = {
    'ru': {
        'proposal': 'Запросить коммерческое предложение',
        'callback': 'Заказать звонок',
        'volunteer': 'Анкета добровольца',
        'team': 'Стать частью команды',
        'review': 'Оставить отзыв',
        'study': 'Записаться на исследование',
        'question': 'Задать вопрос',
    },
    'en': {
        'proposal': 'Request a proposal',
        'callback': 'Request a callback',
        'volunteer': 'Volunteer form',
        'team': 'Join the team',
        'review': 'Leave feedback',
        'study': 'Apply for a study',
        'question': 'Ask a question',
    },
}


def lead_form_config(
    language,
    *,
    title=None,
    lead=None,
    default_type='proposal',
    types=None,
):
    labels = LEAD_TYPE_LABELS[language]
    selected_types = types or ('proposal', 'callback', 'question')
    return {
        'eyebrow': 'Request' if language == 'en' else 'Заявка',
        'title': title or ('Contact CLINISS' if language == 'en' else 'Связаться с CLINISS'),
        'lead': lead or '',
        'default_type': default_type,
        'types': [
            {'value': lead_type, 'label': labels[lead_type]}
            for lead_type in selected_types
        ],
        'submit_label': 'Send Request' if language == 'en' else 'Отправить заявку',
    }


def page(
    slug,
    language,
    title,
    nav_title,
    eyebrow,
    hero_title,
    hero_lead,
    sections,
    *,
    cta_label=None,
    show_lead_form=True,
    hero_image=None,
    stats=None,
    form_title=None,
    form_lead=None,
    default_lead_type='proposal',
    lead_types=None,
):
    return {
        'slug': slug,
        'language': language,
        'title': title,
        'nav_title': nav_title,
        'eyebrow': eyebrow,
        'hero_title': hero_title,
        'hero_lead': hero_lead,
        'sections': sections,
        'cta_label': cta_label,
        'show_lead_form': show_lead_form,
        'hero_image': hero_image,
        'stats': stats or [],
        'lead_form': lead_form_config(
            language,
            title=form_title,
            lead=form_lead,
            default_type=default_lead_type,
            types=lead_types,
        ),
        'alternate_slug': LANGUAGE_PAIRS.get(slug),
    }


def media(src, alt, caption=''):
    return {'src': src, 'alt': alt, 'caption': caption}


def fact(value, label):
    return {'value': value, 'label': label}


def card(title, text='', *, meta='', image='', alt='', value=''):
    return {
        'title': title,
        'text': text,
        'meta': meta,
        'image': image,
        'alt': alt,
        'value': value,
    }


def link(label, url, note='', external=True):
    return {'label': label, 'url': url, 'note': note, 'external': external}


def map_block(title, address, url, embed_url, button_label, note=''):
    return {
        'title': title,
        'address': address,
        'url': url,
        'embed_url': embed_url,
        'button_label': button_label,
        'note': note,
    }


TEAM_RU = [
    card('Устинья Жидкова', meta='менеджер по развитию бизнеса', image='site/img/team/ustinya-zhidkova.png'),
    card('Евгений Хайтович', meta='заместитель директора по клиническим исследованиям', image='site/img/team/evgeny-khaitovich.png'),
    card('Филиппова Полина', meta='заведующий отделением клинических исследований', image='site/img/team/polina-filippova.png'),
    card('Романова Анастасия', meta='менеджер по качеству', image='site/img/team/anastasia-romanova.png'),
    card('Зарифа Мустафаева', meta='медицинская сестра-регистратор', image='site/img/team/zarifa-mustafaeva.png'),
    card('Александрова Виктория', meta='медицинская сестра', image='site/img/team/victoria-aleksandrova.webp'),
    card('Гузаревич Любовь', meta='научный консультант', image='site/img/team/lubov-guzarevich.png'),
    card('Рыжова Снежана', meta='врач-кардиолог', image='site/img/team/snezhana-ryzhova.png'),
    card('Назарова Валерия', meta='врач-терапевт', image='site/img/team/valeria-nazarova.png'),
]

TEAM_EN = [
    card('Ustinia Zhidkova', meta='business development manager', image='site/img/team/ustinya-zhidkova.png'),
    card('Eugene Khaitovich', meta='deputy director for clinical trials', image='site/img/team/evgeny-khaitovich.png'),
    card('Polina Filippova', meta='head of clinical research department', image='site/img/team/polina-filippova.png'),
    card('Anastasia Romanova', meta='quality manager', image='site/img/team/anastasia-romanova.png'),
    card('Zarifa Mustafaeva', meta='registration nurse', image='site/img/team/zarifa-mustafaeva.png'),
    card('Victoria Aleksandrova', meta='nurse', image='site/img/team/victoria-aleksandrova.webp'),
    card('Lubov Guzarevich', meta='scientific consultant', image='site/img/team/lubov-guzarevich.png'),
    card('Snezhana Ryzhova', meta='cardiologist', image='site/img/team/snezhana-ryzhova.png'),
    card('Valeria Nazarova', meta='general practitioner', image='site/img/team/valeria-nazarova.png'),
]

CENTER_FACTS_RU = [
    fact('54', 'койко-места в палатах для добровольцев'),
    fact('3', 'холодовые центрифуги ThermoFisher'),
    fact('-40/-80°C', 'морозильное оборудование Haier'),
    fact('GCP', 'работа по международным стандартам исследований'),
]

CENTER_FACTS_EN = [
    fact('54', 'volunteer beds in the inpatient department'),
    fact('3', 'ThermoFisher refrigerated centrifuges'),
    fact('-40/-80°C', 'Haier freezer equipment'),
    fact('GCP', 'clinical trial processes aligned with global standards'),
]

AREAS_RU = [
    card('Функциональная диагностика', 'Комплексные исследования для оценки и мониторинга работы органов и систем организма.'),
    card('Клинические исследования', 'Оценка безопасности и эффективности новых методов лечения и лекарственных препаратов.'),
    card('Кардиология', 'Исследования и разработка подходов к диагностике и лечению сердечно-сосудистых заболеваний.'),
    card('Психиатрия и наркология', 'Изучение методов диагностики, лечения и поддержки пациентов с психическими расстройствами и зависимостями.'),
    card('Ревматология', 'Исследования заболеваний суставов и соединительных тканей, направленные на снижение боли и улучшение подвижности.'),
    card('Пульмонология', 'Новые методы диагностики и лечения заболеваний органов дыхания.'),
    card('Травматология и ортопедия', 'Исследования восстановления и реабилитации при повреждениях опорно-двигательного аппарата.'),
    card('Клиническая фармакология', 'Изучение воздействия лекарственных препаратов на организм, их эффективности и безопасности.'),
    card('Неврология', 'Новые подходы к диагностике и лечению заболеваний нервной системы.'),
]

AREAS_EN = [
    card('Functional Diagnostics', 'Comprehensive testing to assess and monitor the function of organs and body systems.'),
    card('Clinical Trials', 'Safety and efficacy evaluation of new treatment methods and medicines.'),
    card('Cardiology', 'Research and development of approaches for cardiovascular diagnostics and therapy.'),
    card('Psychiatry and Narcology', 'Diagnostics, treatment, and patient support in mental health and addiction studies.'),
    card('Rheumatology', 'Studies focused on joint and connective tissue diseases, pain reduction, and mobility.'),
    card('Pulmonology', 'New diagnostics and treatment methods for respiratory diseases.'),
    card('Traumatology and Orthopedics', 'Recovery and rehabilitation studies for musculoskeletal injuries.'),
    card('Clinical Pharmacology', 'Assessment of drug effects, safety, efficacy, and treatment optimization.'),
    card('Neurology', 'New approaches to diagnostics and treatment of nervous system diseases.'),
]

VOLUNTEER_FAQ_RU = [
    {
        'question': 'Что я получу за участие в исследованиях?',
        'answer': 'Интересно проведенное время, новые знакомства, бесплатную проверку здоровья и денежную компенсацию.',
    },
    {
        'question': 'Безопасны ли клинические исследования?',
        'answer': 'Центр работает только с исследованиями, прошедшими необходимую оценку безопасности. Добровольца не включают в исследование при состояниях, которые могут повысить риск.',
    },
    {
        'question': 'Кто будет иметь доступ к персональным данным?',
        'answer': 'Персональные и медицинские данные защищаются. При включении в исследование данные добровольца кодируются.',
    },
    {
        'question': 'Могу ли я привести с собой друзей или членов семьи?',
        'answer': 'Да, если они соответствуют требованиям конкретного исследования. Каждый кандидат проходит отдельную анкету, информирование и скрининг.',
    },
    {
        'question': 'Как долго длится исследование?',
        'answer': 'Срок зависит от протокола. Обычно есть стартовый визит, обследования и несколько визитов с пребыванием в центре от 24 до 48 часов.',
    },
    {
        'question': 'Что такое клиническое исследование?',
        'answer': 'Это заранее спланированное изучение лекарственного препарата или метода лечения с участием добровольцев и строгим медицинским наблюдением.',
    },
    {
        'question': 'Может ли участие навредить мне?',
        'answer': 'Перед включением оцениваются противопоказания и риски. Доброволец может отказаться от участия, а команда центра наблюдает за состоянием на каждом этапе.',
    },
    {
        'question': 'Как часто можно участвовать?',
        'answer': 'Как правило, участвовать в клинических исследованиях можно раз в 3 месяца и нельзя быть участником двух исследований одновременно.',
    },
    {
        'question': 'Что если я принимаю другие лекарства?',
        'answer': 'Обязательно сообщите об этом менеджеру и врачу. Решение об участии принимается только после медицинской оценки и требований протокола.',
    },
    {
        'question': 'У меня есть вредные привычки. Это повлияет на участие?',
        'answer': 'Возможность участия зависит от конкретного исследования, результатов скрининга и критериев включения.',
    },
    {
        'question': 'Что такое денежное вознаграждение?',
        'answer': 'Это компенсация за время и соблюдение процедур исследования. Размер и порядок выплаты зависят от протокола.',
    },
    {
        'question': 'Что делать, если я согласен с условиями?',
        'answer': 'Заполните анкету добровольца или закажите обратный звонок. Менеджер свяжется с вами и расскажет о ближайших наборах.',
    },
]

VOLUNTEER_FAQ_EN = [
    {
        'question': 'What will I get for participating?',
        'answer': 'A useful health check, new connections, time spent comfortably at the center, and financial compensation.',
    },
    {
        'question': 'Are clinical trials safe?',
        'answer': 'The center works with studies that have passed the required safety assessment. A volunteer will not be enrolled if medical findings increase risk.',
    },
    {
        'question': 'Who can access my personal data?',
        'answer': 'Personal and medical data are protected. Once enrolled, volunteer data are coded.',
    },
    {
        'question': 'Can I bring friends or family members?',
        'answer': 'Yes, if they meet the requirements of a specific study. Every candidate completes a separate form, consent process, and screening.',
    },
    {
        'question': 'How long does a study take?',
        'answer': 'Timing depends on the protocol. Usually there is a start visit, medical checks, and several visits with a 24 to 48 hour stay at the center.',
    },
    {
        'question': 'What is a clinical study?',
        'answer': 'It is a planned evaluation of a medicine or treatment method involving volunteers and strict medical supervision.',
    },
    {
        'question': 'Can participation harm me?',
        'answer': 'Risks and contraindications are assessed before enrollment. A volunteer may withdraw, and the center team monitors health throughout the study.',
    },
    {
        'question': 'How often can I participate?',
        'answer': 'Usually once every 3 months, and a volunteer cannot participate in two studies at the same time.',
    },
    {
        'question': 'What if I take other medicines?',
        'answer': 'Tell the manager and physician about all medicines. Participation is decided only after medical assessment and protocol review.',
    },
    {
        'question': 'Can habits affect participation?',
        'answer': 'Eligibility depends on the study protocol, screening results, and inclusion criteria.',
    },
    {
        'question': 'What is financial compensation?',
        'answer': 'It is compensation for time and study procedures. The amount and payment process depend on the protocol.',
    },
    {
        'question': 'What should I do if I agree with the conditions?',
        'answer': 'Fill out the volunteer form or request a callback. A manager will contact you and explain current recruitment options.',
    },
]

DOC_LINKS_RU = [
    link('Перечень жизненно необходимых и важнейших лекарственных препаратов', 'https://normativ.kontur.ru/document?moduleId=1&documentId=491464#l17', 'Контур.Норматив'),
    link('Перечень лекарственных препаратов для отдельных категорий заболеваний', 'https://normativ.kontur.ru/document?moduleId=1&documentId=491464#l5559', 'Контур.Норматив'),
    link('Перечень групп населения с 50-процентной скидкой на лекарства', 'https://normativ.kontur.ru/document?moduleId=1&documentId=61472#l1103', 'Контур.Норматив'),
    link('Лицензия организации на сайте Росздравнадзора', 'https://roszdravnadzor.gov.ru/services/licenses?qrguid=3b7bfa5fa5ada8922d28ae1d74d0ebd5', 'Росздравнадзор'),
    link('Структура организации', 'https://disk.yandex.ru/i/V63Iu60aFevphA', 'Яндекс.Диск'),
    link('Программа государственных гарантий медицинской помощи', 'https://www.garant.ru/products/ipo/prime/doc/411138101/', 'Гарант'),
    link('Сведения о медицинских работниках', 'https://disk.yandex.ru/i/qh_t2MgV98YNGA', 'Яндекс.Диск'),
    link('Политика об обработке персональных данных', 'https://disk.yandex.ru/i/zNO3XYku2JzNeg', 'Яндекс.Диск'),
    link('Информированное добровольное согласие на медицинское вмешательство', 'https://disk.yandex.ru/i/oEXu78YjBmLc4g', 'Яндекс.Диск'),
]

DOC_LINKS_EN = [
    link('Vital and Essential Medicines List', 'https://normativ.kontur.ru/document?moduleId=1&documentId=491464#l17', 'Kontur.Normativ'),
    link('Medicines for Certain Disease Categories', 'https://normativ.kontur.ru/document?moduleId=1&documentId=491464#l5559', 'Kontur.Normativ'),
    link('Medicine Discount Eligibility List', 'https://normativ.kontur.ru/document?moduleId=1&documentId=61472#l1103', 'Kontur.Normativ'),
    link('Organization License at Roszdravnadzor', 'https://roszdravnadzor.gov.ru/services/licenses?qrguid=3b7bfa5fa5ada8922d28ae1d74d0ebd5', 'Roszdravnadzor'),
    link('Organizational Structure', 'https://disk.yandex.ru/i/V63Iu60aFevphA', 'Yandex Disk'),
    link('State Guarantees Program for Medical Care', 'https://www.garant.ru/products/ipo/prime/doc/411138101/', 'Garant'),
    link('Medical Staff Details', 'https://disk.yandex.ru/i/qh_t2MgV98YNGA', 'Yandex Disk'),
    link('Personal Data Processing Policy', 'https://disk.yandex.ru/i/zNO3XYku2JzNeg', 'Yandex Disk'),
    link('Informed Voluntary Consent for Medical Intervention', 'https://disk.yandex.ru/i/oEXu78YjBmLc4g', 'Yandex Disk'),
]

CONTACT_LINKS_RU = [
    link('Телефон центра', 'tel:+74822781767', '+7 (4822) 78-17-67', external=False),
    link('Мобильный телефон', 'tel:+79091578618', '+7 (909) 157-86-18', external=False),
    link('Email', 'mailto:info@arsclinic.ru', 'info@arsclinic.ru', external=False),
    link('Telegram', 'https://t.me/cliniss_tver', 'Канал связи с центром'),
    link('WhatsApp', 'https://wa.me/74822781767', 'Быстрое сообщение'),
    link('VK', 'https://vk.com/cliniss_tver', 'Сообщество CLINISS'),
]

CONTACT_LINKS_EN = [
    link('Center phone', 'tel:+74822781767', '+7 (4822) 78-17-67', external=False),
    link('Mobile phone', 'tel:+79091578618', '+7 (909) 157-86-18', external=False),
    link('Email', 'mailto:info@arsclinic.ru', 'info@arsclinic.ru', external=False),
    link('Telegram', 'https://t.me/cliniss_tver', 'Contact channel'),
    link('WhatsApp', 'https://wa.me/74822781767', 'Quick message'),
    link('VK', 'https://vk.com/cliniss_tver', 'CLINISS community'),
]

CONTACT_MAP_RU = map_block(
    'CLINISS на карте',
    '170100, г. Тверь, Вагжановский переулок, 9, 2 этаж',
    'https://yandex.ru/maps/?text=170100%2C%20%D0%A2%D0%B2%D0%B5%D1%80%D1%8C%2C%20%D0%92%D0%B0%D0%B3%D0%B6%D0%B0%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D0%B5%D1%80%D0%B5%D1%83%D0%BB%D0%BE%D0%BA%2C%209',
    'https://yandex.ru/map-widget/v1/?text=170100%2C%20%D0%A2%D0%B2%D0%B5%D1%80%D1%8C%2C%20%D0%92%D0%B0%D0%B3%D0%B6%D0%B0%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D0%B5%D1%80%D0%B5%D1%83%D0%BB%D0%BE%D0%BA%2C%209&z=16',
    'Открыть в Яндекс Картах',
    'Вход в центр расположен на 2 этаже. Перед визитом на скрининг дождитесь подтверждения времени от менеджера.',
)

CONTACT_MAP_EN = map_block(
    'CLINISS on the Map',
    '2nd floor, 9 Vagzhanovsky lane, Tver, Russian Federation, 170100',
    'https://yandex.ru/maps/?text=170100%2C%20Tver%2C%209%20Vagzhanovsky%20lane',
    'https://yandex.ru/map-widget/v1/?text=170100%2C%20Tver%2C%209%20Vagzhanovsky%20lane&z=16',
    'Open in Yandex Maps',
    'The center is located on the 2nd floor. Please wait for the manager to confirm your screening time before visiting.',
)


PAGES = {
    '': page(
        '',
        'ru',
        'CLINISS - современный центр клинических исследований',
        'Главная',
        'Современный центр клинических исследований',
        'CLINISS',
        'Центр клинических исследований биоэквивалентности и ранних фаз с современным оборудованием, технологичной инфраструктурой и командой специалистов.',
        [
            {
                'title': 'О центре',
                'body': [
                    'CLINISS оснащен новейшим оборудованием и ориентирован на проведение исследований биоэквивалентности, ранних фаз, эффективности, безопасности и терапевтической эквивалентности.',
                    'В центре предусмотрены стационарное и амбулаторное отделения, процедурные кабинеты, преаналитическая лаборатория, контролируемый доступ и условия для комфортного пребывания добровольцев.',
                ],
                'facts': CENTER_FACTS_RU,
                'image': media('site/img/photos/lab-tubes.jpg', 'Пробирки в лаборатории CLINISS'),
            },
            {
                'title': 'Клинические исследования',
                'body': [
                    'Исследования проводятся с соблюдением нормативных требований в специально оборудованном современном отделении.',
                ],
                'bullets': ['Биоэквивалентность', 'Терапевтическая эквивалентность', 'Эффективность и безопасность', 'Ранние фазы'],
                'image': media('site/img/photos/center-equipment.png', 'Оборудование CLINISS для хранения и контроля образцов'),
            },
            {
                'title': 'Фотогалерея',
                'body': [
                    'Визуальный ряд перенесен из Tilda-экспорта: реальные помещения центра, зона обследований и палаты для добровольцев.',
                ],
                'images': [
                    media('site/img/photos/outpatient-checkup.jpeg', 'Амбулаторный прием и обследование добровольца'),
                    media('site/img/photos/patient-room.png', 'Палата для добровольцев CLINISS'),
                    media('site/img/photos/center-equipment.png', 'Лабораторное оборудование центра'),
                ],
            },
            {
                'title': 'Для добровольцев',
                'body': [
                    'Центр приглашает добровольцев принять участие в клинических исследованиях. Участники получают медицинское наблюдение, комфортные условия пребывания и денежную компенсацию, если это предусмотрено протоколом.',
                ],
                'image': media('site/img/photos/doctor-documents.jpeg', 'Врач CLINISS работает с документами исследования'),
                'image_position': 'left',
            },
            {
                'title': 'Наша команда',
                'body': [
                    'В проекте участвуют специалисты по клиническим исследованиям, качеству, медицинскому сопровождению и развитию бизнеса.',
                ],
                'cards': TEAM_RU[:6],
                'card_style': 'people',
            },
        ],
        cta_label='Запросить коммерческое предложение',
        hero_image='site/img/hero-lab.jpg',
        stats=[fact('50+', 'завершенных исследований'), fact('600+', 'добровольцев'), fact('54', 'койко-места')],
        form_title='Обсудить исследование',
        form_lead='Оставьте контактные данные, если хотите запросить коммерческое предложение, звонок или консультацию по исследованию.',
        default_lead_type='proposal',
        lead_types=('proposal', 'callback', 'study', 'question'),
    ),
    'en': page(
        'en',
        'en',
        'CLINISS - Modern Clinical Research Center',
        'Home',
        'Modern Clinical Research Center',
        'CLINISS',
        'A clinical research center for bioequivalence and early-phase studies with modern infrastructure, skilled specialists, and transparent processes.',
        [
            {
                'title': 'About the Center',
                'body': [
                    'CLINISS is equipped with modern technology and focuses on bioequivalence, early-phase, efficacy, safety, and therapeutic equivalence studies.',
                    'The center includes inpatient and outpatient departments, procedure rooms, a pre-analytical laboratory, controlled access, and comfortable conditions for volunteers.',
                ],
                'facts': CENTER_FACTS_EN,
                'image': media('site/img/photos/lab-tubes.jpg', 'Laboratory samples at CLINISS'),
            },
            {
                'title': 'Clinical Trials',
                'body': [
                    'Clinical trials are conducted in compliance with regulatory requirements in a specially equipped modern unit.',
                ],
                'bullets': ['Bioequivalence', 'Therapeutic equivalence', 'Efficacy and safety', 'Early phases'],
                'image': media('site/img/photos/center-equipment.png', 'CLINISS equipment for sample storage and control'),
            },
            {
                'title': 'Photo Gallery',
                'body': [
                    'The visual material has been migrated from the Tilda export: real center rooms, screening areas, and volunteer accommodation.',
                ],
                'images': [
                    media('site/img/photos/outpatient-checkup.jpeg', 'Outpatient checkup and volunteer screening'),
                    media('site/img/photos/patient-room.png', 'Volunteer room at CLINISS'),
                    media('site/img/photos/center-equipment.png', 'Center laboratory equipment'),
                ],
            },
            {
                'title': 'For Volunteers',
                'body': [
                    'The center invites volunteers to participate in clinical studies. Participants receive medical supervision, comfortable conditions, and compensation when provided by the protocol.',
                ],
                'image': media('site/img/photos/doctor-documents.jpeg', 'CLINISS doctor working with study documents'),
                'image_position': 'left',
            },
            {
                'title': 'Our Team',
                'body': [
                    'The team includes clinical research, quality, medical support, and business development specialists.',
                ],
                'cards': TEAM_EN[:6],
                'card_style': 'people',
            },
        ],
        cta_label='Request a Proposal',
        hero_image='site/img/hero-lab.jpg',
        stats=[fact('50+', 'completed studies'), fact('600+', 'volunteers'), fact('54', 'beds')],
        form_title='Discuss a Study',
        form_lead='Leave your contact details to request a proposal, callback, or study consultation.',
        default_lead_type='proposal',
        lead_types=('proposal', 'callback', 'study', 'question'),
    ),
    'center': page(
        'center',
        'ru',
        'CLINISS / Наш центр',
        'Наш центр',
        'О центре',
        'Наш центр',
        'Центр ориентирован на проведение клинических исследований биоэквивалентности и обладает широкими возможностями для исследований эффективности, безопасности и терапевтической эквивалентности.',
        [
            {
                'title': 'Инфраструктура и контроль',
                'body': [
                    'Точность исследований обеспечивают современное оборудование, технологичная преаналитическая лаборатория и соблюдение стандартов GCP.',
                    'В центре используются системы дистанционного контроля: HOST CALL для вызова медсестер и врачей, СКУД, Unimon для контроля климата помещений и холодильников, видеоконтроль и синхронизированные часы.',
                ],
                'facts': CENTER_FACTS_RU,
                'image': media('site/img/photos/center-equipment.png', 'Оборудование CLINISS для контроля хранения образцов'),
            },
            {
                'title': 'Амбулаторное отделение',
                'body': ['Отделение включает врачебные кабинеты, процедурный кабинет, сухой туалет для сбора мочи, современное диагностическое оборудование и переговорную комнату.'],
                'bullets': ['Врачебные кабинеты', 'Процедурный кабинет', 'Сбор биоматериала', 'Диагностическое оборудование', 'Переговорная комната'],
                'image': media('site/img/photos/outpatient-checkup.jpeg', 'Амбулаторное обследование добровольца'),
                'image_position': 'left',
            },
            {
                'title': 'Стационарное отделение',
                'body': [
                    'Для участников исследований предусмотрены палаты, реанимационная зона, большой процедурный кабинет, контролируемый доступ, санитарные зоны и система экстренного вызова у каждой койки.',
                ],
                'bullets': ['54 койко-места', 'Палаты для добровольцев', 'Реанимационная зона', 'Контролируемый доступ', 'Санитарные зоны', 'Экстренный вызов'],
                'image': media('site/img/photos/patient-room.png', 'Палата для добровольцев'),
            },
            {
                'title': 'Условия для исследований',
                'body': [
                    'Центр располагает холодовыми центрифугами ThermoFisher, морозильным оборудованием Haier для раздельного хранения архивных и аналитических аликвот, обособленным архивом и комнатами хранения лекарственных средств.',
                ],
                'bullets': ['Преаналитическая лаборатория', 'Хранение -40°C и -80°C', 'Архив', 'Рабочие места для мониторов', 'Wi-Fi с идентификацией пользователей'],
                'image': media('site/img/photos/lab-tubes.jpg', 'Преаналитическая зона CLINISS'),
                'image_position': 'left',
            },
            {
                'title': 'Реквизиты организации',
                'body': [
                    'Общество с ограниченной ответственностью «АРС Клинический Центр». Лицензия на осуществление медицинской деятельности № Л041-01186-69/01327284 от 31.07.2024 г.',
                    'Директор: Тихонов Михаил Юрьевич. ИНН: 7709986403. КПП: 695001001. ОГРН: 1177746054430. Юридический адрес: 170100, Тверская область, г. Тверь, пер. Вагжановский, д. 9, эт/пом 2/1.',
                ],
            },
        ],
        cta_label='Связаться с центром',
        hero_image='site/img/photos/center-equipment.png',
        form_title='Связаться с центром',
        form_lead='Расскажите, какой вопрос хотите обсудить: исследование, визит, документы или партнерство.',
        default_lead_type='callback',
        lead_types=('callback', 'proposal', 'question'),
    ),
    'center-en': page(
        'center-en',
        'en',
        'CLINISS / About the Center',
        'About the Center',
        'About the Center',
        'About the Center',
        'The modern CLINISS center offers bioequivalence, early-phase, therapeutic equivalence, efficacy, and safety studies.',
        [
            {
                'title': 'Infrastructure and Control',
                'body': [
                    'Study accuracy is supported by modern equipment, a technological pre-analytical laboratory, and GCP-aligned procedures.',
                    'The center uses remote monitoring systems, access control, climate monitoring for rooms and freezers, video monitoring, and synchronized clocks.',
                ],
                'facts': CENTER_FACTS_EN,
                'image': media('site/img/photos/center-equipment.png', 'CLINISS equipment for sample storage control'),
            },
            {
                'title': 'Outpatient Department',
                'body': ['The outpatient area includes doctor offices, a procedure room, a dry toilet for urine collection, modern diagnostics, and a meeting room.'],
                'bullets': ['Doctor offices', 'Procedure room', 'Sample collection', 'Diagnostic equipment', 'Meeting room'],
                'image': media('site/img/photos/outpatient-checkup.jpeg', 'Outpatient volunteer checkup'),
                'image_position': 'left',
            },
            {
                'title': 'Inpatient Department',
                'body': ['The inpatient department provides volunteer rooms, an intensive care area, a large procedure room, controlled access, sanitary zones, and emergency call systems.'],
                'bullets': ['54 beds', 'Volunteer rooms', 'Intensive care area', 'Controlled access', 'Sanitary zones', 'Emergency call system'],
                'image': media('site/img/photos/patient-room.png', 'Volunteer room'),
            },
            {
                'title': 'Clinical Trial Conditions',
                'body': ['The center has ThermoFisher refrigerated centrifuges, Haier -40°C and -80°C freezers for separate archival and analytical aliquot storage, an isolated archive, and medicine storage areas.'],
                'bullets': ['Pre-analytical laboratory', '-40°C and -80°C storage', 'Archive', 'Monitor workspaces', 'Wi-Fi with user identification'],
                'image': media('site/img/photos/lab-tubes.jpg', 'CLINISS pre-analytical area'),
                'image_position': 'left',
            },
        ],
        cta_label='Contact the Center',
        hero_image='site/img/photos/center-equipment.png',
        form_title='Contact the Center',
        form_lead='Tell us what you would like to discuss: a study, visit, documents, or partnership.',
        default_lead_type='callback',
        lead_types=('callback', 'proposal', 'question'),
    ),
    'license': page(
        'license',
        'ru',
        'CLINISS / Лицензия',
        'Лицензия',
        'Документы',
        'Лицензия',
        'Лицензия на осуществление медицинской деятельности Л041-01186-69/01327284 от 31.07.2024.',
        [
            {
                'title': 'Медицинская деятельность',
                'body': [
                    'ООО «АРС Клинический Центр» имеет лицензию на осуществление медицинской деятельности № Л041-01186-69/01327284 от 31.07.2024.',
                    'Для публичной проверки доступна ссылка на реестр лицензий Росздравнадзора.',
                ],
                'links': [link('Проверить лицензию на сайте Росздравнадзора', 'https://roszdravnadzor.gov.ru/services/licenses?qrguid=3b7bfa5fa5ada8922d28ae1d74d0ebd5', 'Росздравнадзор')],
            },
            {
                'title': 'Скан-копии',
                'body': ['Из Tilda-экспорта перенесены изображения страниц лицензии.'],
                'images': [
                    media('site/img/documents/license-page-1.png', 'Первая страница лицензии CLINISS'),
                    media('site/img/documents/license-page-2.png', 'Вторая страница лицензии CLINISS'),
                ],
                'gallery_style': 'documents',
            },
        ],
        show_lead_form=False,
        hero_image='site/img/documents/license-page-1.png',
    ),
    'license-en': page(
        'license-en',
        'en',
        'CLINISS / Licenses',
        'Licenses',
        'Documents',
        'Licenses',
        'Medical activity license No. Л041-01186-69/01327284 dated 31.07.2024.',
        [
            {
                'title': 'Medical Activity',
                'body': [
                    'ARS Clinical Center LLC holds medical activity license No. Л041-01186-69/01327284 dated 31.07.2024.',
                    'The public register entry is available through Roszdravnadzor.',
                ],
                'links': [link('Check the license in the Roszdravnadzor register', 'https://roszdravnadzor.gov.ru/services/licenses?qrguid=3b7bfa5fa5ada8922d28ae1d74d0ebd5', 'Roszdravnadzor')],
            },
            {
                'title': 'Scans',
                'body': ['License page images have been migrated from the Tilda export.'],
                'images': [
                    media('site/img/documents/license-page-1.png', 'CLINISS license page one'),
                    media('site/img/documents/license-page-2.png', 'CLINISS license page two'),
                ],
                'gallery_style': 'documents',
            },
        ],
        show_lead_form=False,
        hero_image='site/img/documents/license-page-1.png',
    ),
    'employees': page(
        'employees',
        'ru',
        'CLINISS / Наши сотрудники',
        'Наши сотрудники',
        'Команда',
        'Наши сотрудники',
        'Команда центра включает врачей, специалистов по качеству, клиническим исследованиям, медицинскому сопровождению и развитию бизнеса.',
        [
            {
                'title': 'Специалисты CLINISS',
                'body': ['Карточки сотрудников перенесены из Tilda в структурированный формат с фотографиями и должностями.'],
                'cards': TEAM_RU,
                'card_style': 'people',
            },
            {
                'title': 'Хотите стать частью нашей команды?',
                'body': ['Оставьте заявку, и мы свяжемся с вами, чтобы обсудить возможное сотрудничество и открытые роли.'],
            },
        ],
        cta_label='Стать частью команды',
        hero_image='site/img/graphics/proposal-banner.png',
        stats=[fact('9', 'специалистов в карточках'), fact('GCP', 'опыт исследований'), fact('4', 'ключевых направления команды')],
        form_title='Стать частью команды',
        form_lead='Расскажите о себе и возможном формате сотрудничества с CLINISS.',
        default_lead_type='team',
        lead_types=('team', 'question', 'callback'),
    ),
    'employees-en': page(
        'employees-en',
        'en',
        'CLINISS / Team',
        'Team',
        'Team',
        'Our Team',
        'The center team includes doctors, quality specialists, clinical research staff, medical support, and business development specialists.',
        [
            {
                'title': 'CLINISS Specialists',
                'body': ['Employee cards have been migrated from Tilda into a structured format with photos and roles.'],
                'cards': TEAM_EN,
                'card_style': 'people',
            },
            {
                'title': 'Want to Become Part of the Team?',
                'body': ['Submit a request and we will contact you to discuss possible cooperation and open roles.'],
            },
        ],
        cta_label='Become Part of the Team',
        hero_image='site/img/graphics/proposal-banner.png',
        stats=[fact('9', 'specialists in profiles'), fact('GCP', 'clinical trial experience'), fact('4', 'key team areas')],
        form_title='Become Part of the Team',
        form_lead='Tell us about yourself and the possible cooperation format with CLINISS.',
        default_lead_type='team',
        lead_types=('team', 'question', 'callback'),
    ),
    'missions': page(
        'missions',
        'ru',
        'CLINISS / Наша миссия',
        'Миссия',
        'Ценности',
        'Наша миссия',
        'Внести вклад в развитие медицины и улучшить здоровье людей.',
        [
            {
                'title': 'Миссия и ценности',
                'body': ['CLINISS строит работу вокруг открытости, честности, развития и уважения к человеку.'],
                'cards': [
                    card('Открытость', 'Наши двери открыты: мы доступны партнерам, клиентам, новым сотрудникам и добровольцам.'),
                    card('Настройка', 'Мы открыты новым идеям, готовы к экспериментам и умеем находить нестандартные решения.'),
                    card('Совершенствование', 'Мы учимся, развиваем навыки и используем современные научные и технологические подходы.'),
                    card('Человек', 'Главная ценность - добровольцы, пациенты, сотрудники, клиенты и партнеры.'),
                ],
                'image': media('site/img/graphics/cliniss-wave-brand.jpg', 'Фирменная графика CLINISS'),
            }
        ],
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
        form_title='Связаться по вопросам сотрудничества',
        form_lead='Напишите, если хотите обсудить партнерство, работу центра или участие в исследованиях.',
        default_lead_type='question',
        lead_types=('question', 'callback', 'proposal', 'volunteer'),
    ),
    'missions-en': page(
        'missions-en',
        'en',
        'CLINISS / Mission',
        'Mission',
        'Values',
        'Mission',
        "To contribute to the advancement of medicine and improve people's health.",
        [
            {
                'title': 'Mission and Values',
                'body': ['CLINISS builds its work around accessibility, openness, refinement, and respect for people.'],
                'cards': [
                    card('Accessibility', 'Our doors are open to partners, clients, employees, and volunteers.'),
                    card('Tuning', 'We stay open to new ideas, experiments, and unconventional solutions.'),
                    card('Refinement', 'We learn, improve skills, and use modern scientific and technological approaches.'),
                    card('Person', 'Our main value is the person: volunteers, patients, employees, clients, and partners.'),
                ],
                'image': media('site/img/graphics/cliniss-wave-brand.jpg', 'CLINISS brand graphic'),
            }
        ],
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
        form_title='Contact Us About Cooperation',
        form_lead='Write to discuss partnership, center operations, or participation in studies.',
        default_lead_type='question',
        lead_types=('question', 'callback', 'proposal', 'volunteer'),
    ),
    'system': page(
        'system',
        'ru',
        'CLINISS / Система качества',
        'Система качества',
        'Качество',
        'Система качества',
        'Система качества CLINISS развивается на основе международного стандарта ISO 9001:2015 и регуляторных требований.',
        [
            {
                'title': 'Цели системы качества',
                'body': [
                    'Система качества CLINISS имеет две взаимосвязанные цели: соответствовать нормативным требованиям и постоянно повышать эффективность и конкурентоспособность.',
                ],
                'bullets': ['Стандарты и регламенты', 'Контроль процессов', 'Планирование качества', 'Обеспечение качества', 'Контроль качества', 'Улучшение качества'],
                'cards': [
                    card('Отвечать требованиям', 'Регуляторные и нормативные требования учитываются в процедурах, документации и ежедневном контроле.'),
                    card('Повышать эффективность', 'Процессы регулярно пересматриваются, чтобы сохранять конкурентоспособность и устойчивое качество исследований.'),
                ],
                'image': media('site/img/photos/center-equipment.png', 'Контроль оборудования и условий хранения'),
            }
        ],
        hero_image='site/img/photos/center-equipment.png',
        form_title='Задать вопрос о системе качества',
        form_lead='Оставьте вопрос по стандартам, процедурам или требованиям к проведению исследований.',
        default_lead_type='question',
        lead_types=('question', 'proposal', 'callback'),
    ),
    'system-en': page(
        'system-en',
        'en',
        'CLINISS / Quality Management System',
        'Quality Management System',
        'Quality',
        'Quality Management System',
        'The CLINISS quality management system is developed around ISO 9001:2015 and regulatory requirements.',
        [
            {
                'title': 'Quality Goals',
                'body': [
                    'The CLINISS quality management system has two interconnected goals: meet regulatory requirements and continuously improve effectiveness and competitiveness.',
                ],
                'bullets': ['Standards and regulations', 'Process control', 'Quality planning', 'Quality assurance', 'Quality control', 'Quality improvement'],
                'cards': [
                    card('Meet Requirements', 'Regulatory requirements are reflected in procedures, documentation, and day-to-day control.'),
                    card('Improve Effectiveness', 'Processes are reviewed to maintain competitiveness and stable clinical trial quality.'),
                ],
                'image': media('site/img/photos/center-equipment.png', 'Equipment and storage condition control'),
            }
        ],
        hero_image='site/img/photos/center-equipment.png',
        form_title='Ask About Quality Management',
        form_lead='Leave a question about standards, procedures, or clinical trial requirements.',
        default_lead_type='question',
        lead_types=('question', 'proposal', 'callback'),
    ),
    'areaswork': page(
        'areaswork',
        'ru',
        'CLINISS / Направления работы',
        'Направления работы',
        'Услуги',
        'Направления работы',
        'Центр проводит широкий спектр научных исследований, направленных на развитие медицины и внедрение новых решений.',
        [
            {
                'title': 'Исследовательские направления',
                'body': [
                    'CLINISS стремится к созданию и внедрению решений, которые могут улучшить качество жизни людей и дать новый импульс развитию медицинских технологий.',
                ],
                'cards': AREAS_RU,
                'card_style': 'compact',
                'image': media('site/img/photos/bioequivalence-lab.png', 'Лабораторная работа с образцами'),
            },
            {
                'title': 'Для добровольцев',
                'body': [
                    'Мы ищем добровольцев для участия в клинических исследованиях. Это возможность внести вклад в развитие медицины и помочь улучшить здоровье миллионов людей.',
                ],
                'links': [link('Узнать больше', '/volunteers', 'Раздел для добровольцев', external=False)],
                'image': media('site/img/photos/volunteer-path.png', 'Путь добровольца в исследовании'),
                'image_position': 'left',
            },
        ],
        cta_label='Запросить предложение',
        hero_image='site/img/photos/research-hero.png',
        form_title='Запросить предложение',
        form_lead='Опишите интересующее направление, протокол или задачу, чтобы команда подготовила следующий шаг.',
        default_lead_type='proposal',
        lead_types=('proposal', 'study', 'question', 'callback'),
    ),
    'areaswork-en': page(
        'areaswork-en',
        'en',
        'CLINISS / Areas of Work',
        'Areas of Work',
        'Services',
        'Areas of Work',
        'The center conducts a broad range of scientific studies aimed at medical development and implementation of new solutions.',
        [
            {
                'title': 'Research Areas',
                'body': [
                    'CLINISS focuses on solutions that can improve quality of life and support the development of medical technologies.',
                ],
                'cards': AREAS_EN,
                'card_style': 'compact',
                'image': media('site/img/photos/bioequivalence-lab.png', 'Laboratory work with samples'),
            },
            {
                'title': 'For Volunteers',
                'body': ['We invite volunteers to participate in clinical studies and contribute to the future of medicine.'],
                'links': [link('Learn more', '/volunteers-en', 'Volunteer section', external=False)],
                'image': media('site/img/photos/volunteer-path.png', 'Volunteer pathway in a study'),
                'image_position': 'left',
            },
        ],
        cta_label='Request a Proposal',
        hero_image='site/img/photos/research-hero.png',
        form_title='Request a Proposal',
        form_lead='Describe the area, protocol, or task of interest so the team can prepare the next step.',
        default_lead_type='proposal',
        lead_types=('proposal', 'study', 'question', 'callback'),
    ),
    'price': page(
        'price',
        'ru',
        'CLINISS / Прайс',
        'Прайс',
        'Стоимость',
        'Прайс',
        'Цены зависят от протокола, состава процедур, сроков и требований исследования.',
        [
            {
                'title': 'Коммерческое предложение',
                'body': [
                    'Центр готов предоставить подробную информацию об услугах и исследованиях. Мы предлагаем прозрачные и конкурентные условия, соответствующие высокому качеству и стандартам медицинских исследований.',
                    'Для детальной информации о расчетах, возможных скидках и составе работ свяжитесь с нами или запросите обратный звонок.',
                ],
                'bullets': ['Исследования биоэквивалентности', 'Ранние фазы', 'Эффективность и безопасность', 'Терапевтическая эквивалентность'],
                'cards': [
                    card('Расчет по протоколу', 'Стоимость зависит от дизайна исследования, числа периодов, процедур, длительности пребывания и требований к отчетности.'),
                    card('Коммерческое предложение', 'Команда подготовит предложение после уточнения задач, сроков, объема медицинских процедур и логистики образцов.'),
                ],
                'image': media('site/img/graphics/proposal-banner.png', 'Фирменный баннер CLINISS для коммерческого предложения'),
            }
        ],
        cta_label='Запросить коммерческое предложение',
        hero_image='site/img/graphics/proposal-banner.png',
        form_title='Запросить коммерческое предложение',
        form_lead='Оставьте вводные по исследованию: команда уточнит протокол, сроки, процедуры и логистику образцов.',
        default_lead_type='proposal',
        lead_types=('proposal', 'callback', 'question'),
    ),
    'price-en': page(
        'price-en',
        'en',
        'CLINISS / Price',
        'Price',
        'Pricing',
        'Price',
        'Pricing depends on the protocol, procedures, timelines, and study requirements.',
        [
            {
                'title': 'Commercial Proposal',
                'body': [
                    'The center is ready to provide detailed information about services and trials. We offer transparent and competitive conditions aligned with high medical research standards.',
                    'For detailed calculations, possible discounts, and scope of work, contact us or request a callback.',
                ],
                'bullets': ['Bioequivalence studies', 'Early phases', 'Efficacy and safety', 'Therapeutic equivalence'],
                'cards': [
                    card('Protocol-Based Estimate', 'Pricing depends on study design, number of periods, procedures, length of stay, and reporting requirements.'),
                    card('Commercial Proposal', 'The team prepares a proposal after clarifying objectives, timelines, medical procedures, and sample logistics.'),
                ],
                'image': media('site/img/graphics/proposal-banner.png', 'CLINISS proposal banner'),
            }
        ],
        cta_label='Request a Proposal',
        hero_image='site/img/graphics/proposal-banner.png',
        form_title='Request a Commercial Proposal',
        form_lead='Share initial study details: the team will clarify protocol, timeline, procedures, and sample logistics.',
        default_lead_type='proposal',
        lead_types=('proposal', 'callback', 'question'),
    ),
    'volunteers': page(
        'volunteers',
        'ru',
        'CLINISS / Для добровольцев',
        'Для добровольцев',
        'Добровольцам',
        'Хочешь стать добровольцем?',
        'Участие в клинических исследованиях помогает современной медицине и дает возможность проконтролировать состояние здоровья.',
        [
            {
                'title': 'Почему участвуют',
                'body': [
                    'Во время исследования у вас будет возможность проконтролировать и оценить состояние своего здоровья, познакомиться с новыми людьми и провести время с пользой.',
                    'Участие здоровых добровольцев в клинических исследованиях оплачивается, если это предусмотрено конкретным протоколом.',
                ],
                'image': media('site/img/photos/volunteer-path.png', 'Путь добровольца в клиническом исследовании'),
            },
            {
                'title': 'Часто задаваемые вопросы',
                'body': ['Мы собрали основные вопросы, которые добровольцы задают перед участием в исследованиях.'],
                'faq': VOLUNTEER_FAQ_RU,
            },
            {
                'title': 'Кому подходит участие',
                'body': [
                    'К участию приглашаются лица старше 18 лет без острых заболеваний и без противопоказаний по критериям конкретного протокола.',
                    'Перед включением доброволец проходит информированное согласие, медицинский осмотр и скрининг.',
                ],
                'bullets': ['Старше 18 лет', 'Без острых заболеваний', 'Без противопоказаний протокола', 'Информированное согласие', 'Медицинский скрининг'],
                'image': media('site/img/photos/outpatient-checkup.jpeg', 'Скрининг добровольца в CLINISS'),
                'image_position': 'left',
            },
            {
                'title': 'Как стать добровольцем',
                'body': [
                    'Достаточно заполнить анкету или заказать обратный звонок. Мы свяжемся с вами, уточним данные и расскажем о ближайших исследованиях.',
                    'Добровольцами могут стать лица старше 18 лет без острых и хронических заболеваний. Беременные и кормящие женщины не участвуют в исследованиях в нашем центре.',
                ],
                'bullets': ['Анкета', 'Обратный звонок', 'Информированное согласие', 'Скрининг', 'Участие по протоколу'],
            },
        ],
        cta_label='Заполнить анкету добровольца',
        hero_image='site/img/photos/volunteer-path.png',
        stats=[fact('18+', 'возраст добровольцев'), fact('3 мес.', 'обычный интервал участия'), fact('24-48 ч', 'частый формат пребывания')],
        form_title='Анкета добровольца',
        form_lead='Оставьте контакты, чтобы менеджер рассказал о ближайших наборах и условиях скрининга.',
        default_lead_type='volunteer',
        lead_types=('volunteer', 'callback', 'study', 'question'),
    ),
    'volunteers-en': page(
        'volunteers-en',
        'en',
        'CLINISS / For Volunteers',
        'For Volunteers',
        'Volunteers',
        'Want to Become a Volunteer?',
        'Participation in clinical studies supports modern medicine and gives you an opportunity to check your health.',
        [
            {
                'title': 'Why People Participate',
                'body': [
                    'During a study you can check your health, meet new people, and spend time usefully.',
                    'Participation of healthy volunteers is compensated when provided by the study protocol.',
                ],
                'image': media('site/img/photos/volunteer-path.png', 'Volunteer pathway in a clinical study'),
            },
            {
                'title': 'FAQ',
                'body': ['Key questions volunteers ask before participating in clinical studies.'],
                'faq': VOLUNTEER_FAQ_EN,
            },
            {
                'title': 'Who Can Participate',
                'body': [
                    'Participation is open to people over 18 without acute diseases and without contraindications under a specific protocol.',
                    'Before enrollment, every volunteer goes through informed consent, medical examination, and screening.',
                ],
                'bullets': ['Over 18 years old', 'No acute diseases', 'No protocol contraindications', 'Informed consent', 'Medical screening'],
                'image': media('site/img/photos/outpatient-checkup.jpeg', 'Volunteer screening at CLINISS'),
                'image_position': 'left',
            },
            {
                'title': 'How to Become a Volunteer',
                'body': [
                    'Fill out a form or request a callback. We will contact you, clarify details, and tell you about upcoming studies.',
                    'Volunteers must be over 18 and free of acute or chronic diseases. Pregnant and breastfeeding women cannot participate in studies at the center.',
                ],
                'bullets': ['Form', 'Callback', 'Informed consent', 'Screening', 'Protocol participation'],
            },
        ],
        cta_label='Fill Out Volunteer Form',
        hero_image='site/img/photos/volunteer-path.png',
        stats=[fact('18+', 'volunteer age'), fact('3 mo.', 'typical interval'), fact('24-48 h', 'common stay format')],
        form_title='Volunteer Form',
        form_lead='Leave your contact details so a manager can explain current recruitment and screening conditions.',
        default_lead_type='volunteer',
        lead_types=('volunteer', 'callback', 'study', 'question'),
    ),
    'contacts': page(
        'contacts',
        'ru',
        'CLINISS / Контакты',
        'Контакты',
        'Контакты',
        'Контакты',
        'Вагжановский переулок, 9, 2 этаж, Тверь. Телефон: +7 (4822) 78-17-67.',
        [
            {
                'title': 'Быстрые контакты',
                'body': [
                    'ООО «АРС Клинический Центр». Лицензия на осуществление медицинской деятельности Л041-01186-69/01327284 от 31.07.2024.',
                    'Адрес: 170100, г. Тверь, Вагжановский переулок, 9, 2 этаж.',
                ],
                'links': CONTACT_LINKS_RU,
                'facts': [
                    fact('10:00-13:00', 'прием граждан в последнюю среду месяца'),
                    fact('2 этаж', 'расположение центра'),
                    fact('122', 'горячая линия Минздрава Тверской области'),
                ],
                'image': media('site/img/photos/contacts-illustration.png', 'Иллюстрация контактов CLINISS'),
            },
            {
                'title': 'Адрес и визит в центр',
                'body': [
                    'Перед визитом на скрининг или встречу дождитесь подтверждения времени от менеджера центра.',
                    'Для вопросов по доступности и качеству медицинской помощи в регионе также работает единый номер горячей линии Министерства здравоохранения Тверской области 122.',
                ],
                'bullets': ['Тверь, Вагжановский переулок, 9', '2 этаж', 'Предварительное согласование визита', 'Связь по телефону, email и мессенджерам'],
                'map': CONTACT_MAP_RU,
            },
        ],
        cta_label='Оставить заявку',
        hero_image='site/img/photos/contacts-illustration.png',
        form_title='Напишите в CLINISS',
        form_lead='Выберите тип обращения, оставьте контакты, и команда центра вернется с ответом.',
        default_lead_type='question',
        lead_types=('question', 'callback', 'proposal', 'volunteer', 'review'),
    ),
    'contacts-en': page(
        'contacts-en',
        'en',
        'CLINISS / Contacts',
        'Contacts',
        'Contacts',
        'Contacts',
        '2nd floor, 9 Vagzhanovsky lane, Tver, Russian Federation. Phone: +7 (4822) 78-17-67.',
        [
            {
                'title': 'Quick Contacts',
                'body': [
                    'ARS Clinical Center LLC. Medical activity license Л041-01186-69/01327284 dated 31.07.2024.',
                    'Address: 2nd floor, 9 Vagzhanovsky lane, Tver, Russian Federation, 170100.',
                ],
                'links': CONTACT_LINKS_EN,
                'facts': [
                    fact('10:00-13:00', 'public reception on the last Wednesday of each month'),
                    fact('2nd floor', 'center location'),
                    fact('122', 'Tver Region Ministry of Health hotline'),
                ],
                'image': media('site/img/photos/contacts-illustration.png', 'CLINISS contact illustration'),
            },
            {
                'title': 'Address and Visit',
                'body': [
                    'Please wait for a manager to confirm the time before coming for screening or a meeting.',
                    'The Tver Region Ministry of Health hotline 122 is also available for questions about access to care and quality of care in the region.',
                ],
                'bullets': ['Tver, 9 Vagzhanovsky lane', '2nd floor', 'Visit confirmed in advance', 'Contact by phone, email, or messengers'],
                'map': CONTACT_MAP_EN,
            },
        ],
        cta_label='Submit a Request',
        hero_image='site/img/photos/contacts-illustration.png',
        form_title='Contact CLINISS',
        form_lead='Choose the request type, leave your contact details, and the center team will reply.',
        default_lead_type='question',
        lead_types=('question', 'callback', 'proposal', 'volunteer', 'review'),
    ),
    'docs': page(
        'docs',
        'ru',
        'CLINISS / Нормативные документы',
        'Нормативные документы',
        'Документы',
        'Нормативные документы',
        'Раздел содержит сведения о контролирующих органах, лекарственном обеспечении, правилах участия и внешние нормативные ссылки.',
        [
            {
                'title': 'Контролирующие органы',
                'body': [
                    'Единый номер горячей линии Министерства здравоохранения Тверской области - 122. По нему можно задать вопросы о доступности и качестве медицинской помощи, лекарственном обеспечении, диспансеризации и профосмотрах.',
                    'Министерство здравоохранения Тверской области: 170100, г. Тверь, улица Ивана Седых, 8; тел./факс: (4822) 33-32-55; dep_zdrav@tverreg.ru.',
                    'Территориальный орган Росздравнадзора по Тверской области: (4822) 35-85-88; rzntver@reg69.roszdravnadzor.gov.ru; 170100, г. Тверь, ул. Советская, д. 35, корпус 1.',
                    'Управление Роспотребнадзора по Тверской области: 170034, г. Тверь, ул. Дарвина, д. 17; тел. (4822) 34-22-11.',
                ],
            },
            {
                'title': 'Лекарственное обеспечение и лицензия',
                'body': [
                    'На странице сохранены внешние ссылки на перечни лекарственных препаратов, сведения о лицензии и документы организации.',
                ],
                'links': DOC_LINKS_RU,
                'images': [
                    media('site/img/documents/organization-structure.png', 'Организационная структура CLINISS'),
                ],
                'gallery_style': 'documents',
            },
            {
                'title': 'Правила участия и оказания услуг',
                'body': [
                    'Запись добровольцев на участие в клинических исследованиях осуществляется после заполнения анкеты на сайте или в официальных социальных сетях центра. После обработки данных менеджер связывается с кандидатом для уточнения деталей и назначения времени визита на скрининг.',
                    'Стандартный консультативный прием граждан вне рамок протоколов клинических исследований в центре не ведется. Обследования и медицинские вмешательства выполняются только для лиц, включенных в программы клинических исследований.',
                    'Центр не участвует в реализации программы ОМС и не ведет прием граждан по полисам обязательного медицинского страхования.',
                ],
                'bullets': ['Запись после анкеты', 'Индивидуальная подготовка по протоколу', 'Госпитализация только в рамках исследования', 'Платные медицинские услуги населению не оказываются', 'ОМС не ведется'],
            },
            {
                'title': 'Прием граждан и согласия',
                'body': [
                    'Прием граждан проводится в последнюю среду месяца с 10:00 до 13:00.',
                    'На исходном сайте отдельно размещены политика об обработке персональных данных и информированное добровольное согласие на медицинское вмешательство. Эти внешние ссылки сохранены в новом разделе документов.',
                ],
                'links': [
                    link('Политика об обработке персональных данных', 'https://disk.yandex.ru/i/zNO3XYku2JzNeg', 'Яндекс.Диск'),
                    link('Информированное добровольное согласие на медицинское вмешательство', 'https://disk.yandex.ru/i/oEXu78YjBmLc4g', 'Яндекс.Диск'),
                    link('Политика конфиденциальности сайта', '/policy', 'Внутренняя страница', external=False),
                    link('Соглашение об обработке персональных данных', '/agreement', 'Внутренняя страница', external=False),
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/documents/organization-structure.png',
    ),
    'docs-en': page(
        'docs-en',
        'en',
        'CLINISS / Regulatory Documents',
        'Documents',
        'Documents',
        'Regulatory Documents',
        'This section contains regulatory authority details, medicine support links, participation rules, and external regulatory references.',
        [
            {
                'title': 'Regulatory Authorities',
                'body': [
                    'The Ministry of Health hotline for the Tver Region is 122. It can be used for questions about access to care, quality of care, medicines, and preventive checkups.',
                    'Tver Region Ministry of Health: 8 Ivan Sedykh St., Tver; phone/fax: (4822) 33-32-55; dep_zdrav@tverreg.ru.',
                    'Roszdravnadzor territorial body for the Tver Region: (4822) 35-85-88; rzntver@reg69.roszdravnadzor.gov.ru; 35 Sovetskaya St., building 1, Tver.',
                    'Rospotrebnadzor for the Tver Region: 17 Darvina St., Tver; phone: (4822) 34-22-11.',
                ],
            },
            {
                'title': 'Medicine Support and License',
                'body': ['External regulatory links from the Russian page are preserved for public reference.'],
                'links': DOC_LINKS_EN,
                'images': [
                    media('site/img/documents/organization-structure.png', 'CLINISS organizational structure'),
                ],
                'gallery_style': 'documents',
            },
            {
                'title': 'Participation and Service Rules',
                'body': [
                    'Volunteer enrollment starts after a form is submitted on the site or through official social channels. A manager contacts the candidate to clarify details and schedule screening.',
                    'The center does not provide routine outpatient consultations outside clinical trial protocols and does not participate in compulsory medical insurance programs.',
                ],
                'bullets': ['Enrollment after form submission', 'Protocol-specific preparation', 'Hospitalization only within a study', 'No paid medical services for the public', 'No compulsory medical insurance reception'],
            },
            {
                'title': 'Public Reception and Consent Forms',
                'body': [
                    'Public reception is held on the last Wednesday of each month from 10:00 to 13:00.',
                    'The original site provides separate downloadable documents for the personal data processing policy and informed voluntary consent for medical intervention. These external links are preserved here.',
                ],
                'links': [
                    link('Personal Data Processing Policy', 'https://disk.yandex.ru/i/zNO3XYku2JzNeg', 'Yandex Disk'),
                    link('Informed Voluntary Consent for Medical Intervention', 'https://disk.yandex.ru/i/oEXu78YjBmLc4g', 'Yandex Disk'),
                    link('Site Privacy Policy', '/policy-en', 'Internal page', external=False),
                    link('Personal Data Processing Agreement', '/agreement-en', 'Internal page', external=False),
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/documents/organization-structure.png',
    ),
    'issledovaniya-bioekvivalentnosti': page(
        'issledovaniya-bioekvivalentnosti',
        'ru',
        'CLINISS / Исследования биоэквивалентности',
        'Исследования биоэквивалентности',
        'Исследования',
        'Исследования биоэквивалентности',
        'Исследования проводятся для сравнения фармакокинетического профиля исследуемого препарата с референтным препаратом.',
        [
            {
                'title': 'Что такое биоэквивалентность',
                'body': [
                    'Исследование проводится для сравнения фармакокинетического профиля исследуемого препарата с уже существующим препаратом и определения их биоэквивалентности.',
                    'CLINISS провел до 50 клинических исследований в области биоэквивалентности, эффективности, безопасности и терапевтической эквивалентности.',
                ],
                'facts': [fact('50', 'завершенных исследований'), fact('600', 'добровольцев успешно прошли исследование')],
                'image': media('site/img/photos/bioequivalence-lab.png', 'Лабораторный анализ биоэквивалентности'),
            },
            {
                'title': 'Путь добровольца',
                'body': ['Участие строится по протоколу исследования и включает несколько этапов от первичного отбора до завершения визитов.'],
                'cards': [
                    card('Рекрутинг', 'Поиск и предварительный отбор добровольцев по основным требованиям исследования.'),
                    card('Скрининг', 'Медицинское обследование, анализы и сбор анамнеза для проверки критериев протокола.'),
                    card('Госпитализация', 'Прибытие в центр и подготовка к активной части исследования.'),
                    card('Дозинг', 'Прием исследуемого препарата под медицинским наблюдением и сбор данных.'),
                    card('Амбулаторные визиты', 'Контрольные осмотры и анализы после выписки.'),
                ],
                'image': media('site/img/photos/bioequivalence-screening.png', 'Скрининг добровольцев'),
                'image_position': 'left',
            },
        ],
        cta_label='Запросить предложение',
        hero_image='site/img/photos/research-hero.png',
        stats=[fact('50', 'исследований'), fact('600', 'добровольцев'), fact('GCP', 'стандарты')],
        form_title='Запросить предложение по биоэквивалентности',
        form_lead='Опишите препарат, формат исследования или вопрос по протоколу, чтобы команда связалась с вами.',
        default_lead_type='proposal',
        lead_types=('proposal', 'study', 'question', 'callback'),
    ),
    'issledovaniya-bioekvivalentnosti-en': page(
        'issledovaniya-bioekvivalentnosti-en',
        'en',
        'CLINISS / Bioequivalence Studies',
        'Bioequivalence Studies',
        'Studies',
        'Bioequivalence Studies',
        'Bioequivalence studies compare the pharmacokinetic profile of an investigational product with a reference product.',
        [
            {
                'title': 'What Bioequivalence Means',
                'body': [
                    'The study compares the pharmacokinetic profile of the investigational medicine with an existing reference product and evaluates their bioequivalence.',
                    'CLINISS has conducted up to 50 clinical studies in bioequivalence, efficacy, safety, and therapeutic equivalence.',
                ],
                'facts': [fact('50', 'completed studies'), fact('600', 'volunteers successfully completed studies')],
                'image': media('site/img/photos/bioequivalence-lab.png', 'Bioequivalence laboratory analysis'),
            },
            {
                'title': 'Volunteer Pathway',
                'body': ['Participation follows a study protocol and includes several stages from initial recruitment to follow-up visits.'],
                'cards': [
                    card('Recruitment', 'Search and preliminary selection of volunteers by study requirements.'),
                    card('Screening', 'Medical checks, tests, and history collection to confirm protocol criteria.'),
                    card('Hospitalization', 'Arrival at the center and preparation for the active study phase.'),
                    card('Dosing', 'Administration of the investigational product under medical supervision.'),
                    card('Outpatient Visits', 'Follow-up examinations and tests after discharge.'),
                ],
                'image': media('site/img/photos/bioequivalence-screening.png', 'Volunteer screening'),
                'image_position': 'left',
            },
        ],
        cta_label='Request a Proposal',
        hero_image='site/img/photos/research-hero.png',
        stats=[fact('50', 'studies'), fact('600', 'volunteers'), fact('GCP', 'standards')],
        form_title='Request a Bioequivalence Proposal',
        form_lead='Describe the medicine, study format, or protocol question so the team can contact you.',
        default_lead_type='proposal',
        lead_types=('proposal', 'study', 'question', 'callback'),
    ),
    'policy': page(
        'policy',
        'ru',
        'Политика конфиденциальности',
        'Политика конфиденциальности',
        'Правовая информация',
        'Политика конфиденциальности',
        'Политика описывает порядок обработки и защиты персональных данных пользователей сайта CLINISS.',
        [
            {
                'title': 'Оператор и общие положения',
                'body': [
                    'Оператором персональных данных является ООО «АРС Клинический Центр». Пользователь может получить разъяснения по вопросам обработки персональных данных по адресу info@arsclinic.ru.',
                    'Политика применяется ко всей информации, которую сайт может получить о пользователе во время использования сайта, форм обратной связи и сервисов коммуникации.',
                ],
            },
            {
                'title': 'Цели и категории данных',
                'body': [
                    'Данные обрабатываются для обратной связи, обработки заявок, записи кандидатов на исследования, ведения внутреннего учета обращений, улучшения качества сайта и выполнения требований законодательства.',
                    'К обрабатываемым данным относятся имя, телефон, email, комментарии пользователя, сведения из форм, технические данные браузера, IP-адрес и cookie.',
                ],
            },
            {
                'title': 'Права пользователя и безопасность',
                'body': [
                    'Пользователь вправе уточнять, блокировать или удалять персональные данные, если они являются неполными, устаревшими, неточными или обрабатываются незаконно.',
                    'Оператор принимает организационные и технические меры для защиты персональных данных от неправомерного доступа, уничтожения, изменения, блокирования, копирования и распространения.',
                ],
            },
            {
                'title': 'Контакты и актуальная версия',
                'body': [
                    'Все изменения политики публикуются на сайте. Актуальная версия расположена по адресу https://cliniss.ru/policy.',
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
    ),
    'policy-en': page(
        'policy-en',
        'en',
        'Privacy Policy',
        'Privacy Policy',
        'Legal',
        'Privacy Policy',
        'This page provides an English reference version of the Russian personal data policy.',
        [
            {
                'title': 'Controller and Scope',
                'body': [
                    'The personal data controller is ARS Clinical Center LLC. Questions about personal data processing can be sent to info@arsclinic.ru.',
                    'The policy applies to information received through the site, feedback forms, and communication channels.',
                ],
            },
            {
                'title': 'Purposes and Data Categories',
                'body': [
                    'Data are processed for feedback, request handling, volunteer enrollment, internal lead accounting, site improvement, and legal compliance.',
                    'Processed data may include name, phone, email, user comments, form data, browser technical data, IP address, and cookies.',
                ],
            },
            {
                'title': 'User Rights and Security',
                'body': [
                    'The user may request clarification, blocking, or deletion of personal data where permitted by law.',
                    'The controller applies organizational and technical measures to protect personal data from unauthorized access and misuse.',
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
    ),
    'agreement': page(
        'agreement',
        'ru',
        'Соглашение об обработке персональных данных',
        'Соглашение',
        'Правовая информация',
        'Соглашение об обработке персональных данных',
        'Соглашение является публичной офертой и используется при отправке форм на сайте CLINISS.',
        [
            {
                'title': 'Термины и согласие',
                'body': [
                    'Сайт - совокупность текстов, графических элементов, дизайна, изображений, программного кода и иных материалов, размещенных по адресу https://cliniss.ru.',
                    'Администрация сайта - ООО «АРС Клинический Центр». Пользователь - лицо, осуществившее доступ к сайту, заполнившее формы обратной связи и принявшее условия соглашения.',
                    'Оставляя данные на сайте, пользователь подтверждает достоверность данных, ознакомление с соглашением, согласие на обработку персональных данных и использование cookie.',
                ],
            },
            {
                'title': 'Цели обработки',
                'body': [
                    'Персональные данные используются для предоставления медицинских и консультационных услуг, обработки заявок и обращений, обратной связи, ведения клиентской базы, информирования об услугах и выполнения требований законодательства РФ.',
                ],
            },
            {
                'title': 'Способы обработки и срок действия',
                'body': [
                    'Обработка осуществляется с использованием средств автоматизации и без них. Администрация сайта вправе вести электронные базы, реестры и внутренние системы учета.',
                    'Согласие действует с момента предоставления данных и до достижения целей обработки либо до отзыва пользователем.',
                ],
            },
            {
                'title': 'Cookie',
                'body': [
                    'Файлы cookie помогают запоминать настройки и улучшать пользовательский опыт. На сайте могут использоваться обязательные, аналитические, функциональные и рекламные cookie при наличии соответствующих сервисов.',
                    'Пользователь может изменить настройки cookie в браузере. Отключение cookie может повлиять на работу отдельных функций сайта.',
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
    ),
    'agreement-en': page(
        'agreement-en',
        'en',
        'Personal Data Processing Agreement',
        'Agreement',
        'Legal',
        'Personal Data Processing Agreement',
        'This English reference page describes the consent used when forms are submitted on the CLINISS site.',
        [
            {
                'title': 'Terms and Consent',
                'body': [
                    'The site is the set of text, design, images, program code, and other materials located at https://cliniss.ru.',
                    'The site administration is ARS Clinical Center LLC. A user is a person who accesses the site, completes feedback forms, and accepts the agreement terms.',
                    'By submitting data, the user confirms data accuracy, acceptance of the agreement, consent to personal data processing, and cookie use.',
                ],
            },
            {
                'title': 'Processing Purposes',
                'body': [
                    'Personal data are used for medical and consultation services, request handling, feedback, internal records, information about services, and compliance with Russian law.',
                ],
            },
            {
                'title': 'Processing and Duration',
                'body': [
                    'Processing may be automated or non-automated. Consent applies from the moment data are submitted until processing purposes are achieved or consent is withdrawn.',
                ],
            },
            {
                'title': 'Cookies',
                'body': [
                    'Cookies help remember settings and improve user experience. Browser settings can be used to limit cookies, but this may affect some site functions.',
                ],
            },
        ],
        show_lead_form=False,
        hero_image='site/img/graphics/cliniss-wave-brand.jpg',
    ),
}

PAGE_ORDER = list(PAGES.keys())


def get_page(slug):
    return PAGES.get(slug or '')


def section_text(section):
    parts = [
        section.get('title', ''),
        ' '.join(section.get('body', [])),
        ' '.join(section.get('bullets', [])),
    ]
    for collection in ('facts', 'cards', 'faq', 'links'):
        for item in section.get(collection, []):
            parts.extend(str(value) for value in item.values())
    return ' '.join(parts)


def search_pages(query):
    normalized = query.strip().lower()
    if not normalized:
        return []

    results = []
    for item in PAGES.values():
        haystack = ' '.join(
            [
                item['title'],
                item['hero_title'],
                item['hero_lead'],
                ' '.join(section_text(section) for section in item['sections']),
            ]
        ).lower()
        if normalized in haystack:
            results.append(item)
    return results

