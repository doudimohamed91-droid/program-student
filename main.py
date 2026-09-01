import flet as ft

from database import init_database

from pages.home import home_page
from pages.reminders import reminders_page
from pages.classes import classes_page
from pages.assignments import assignments_page
from pages.goals import goals_page
from pages.grades import grades_page
from pages.expenses import expenses_page
from pages.notes import notes_page
from pages.links import links_page


# =========================================================
# قاعدة البيانات
# =========================================================

init_database()


# =========================================================
# التطبيق الرئيسي
# =========================================================

def main(page: ft.Page):

    # =====================================================
    # إعدادات التطبيق
    # =====================================================

    page.title = "Student Hub | مساعد الطالب"

    page.padding = 0
    page.spacing = 0

    page.bgcolor = "#EEF2F7"

    # =====================================================
    # حالة الوضع
    # =====================================================

    dark_mode = False

    # =====================================================
    # محتوى الصفحات
    # =====================================================

    page_content = ft.Container(
        expand=True,
        padding=25,
    )

    # =====================================================
    # خلفية التطبيق
    # =====================================================

    background = ft.Container(
        expand=True,
        image=ft.DecorationImage(
            src="icon.jpg",
            fit="cover",
            opacity=0.18,
        ),
    )

    # =====================================================
    # طبقة المحتوى فوق الخلفية
    # =====================================================

    content = ft.Stack(
        [
            background,
            page_content,
        ],
        expand=True,
    )

    # =====================================================
    # عنوان الصفحة
    # =====================================================

    page_title = ft.Text(
        "الرئيسية",
        size=25,
        weight=ft.FontWeight.BOLD,
        color="#172033",
    )

    page_subtitle = ft.Text(
        "نظرة سريعة على يومك الدراسي",
        size=14,
        color="#667085",
    )

    # =====================================================
    # حالة التطبيق
    # =====================================================

    status_text = ft.Text(
        "جاهز",
        size=12,
        color="#667085",
    )

    # =====================================================
    # زر الوضع الليلي
    # =====================================================

    theme_button = ft.IconButton(
        icon=ft.Icons.DARK_MODE_OUTLINED,
        tooltip="الوضع الليلي",
        icon_color="#344054",
    )

    # =====================================================
    # عناصر القائمة
    # =====================================================

    menu_items = [

        (
            "الرئيسية",
            ft.Icons.HOME_OUTLINED,
            ft.Icons.HOME,
        ),

        (
            "التذكيرات",
            ft.Icons.NOTIFICATIONS_OUTLINED,
            ft.Icons.NOTIFICATIONS,
        ),

        (
            "جدول الحصص",
            ft.Icons.CALENDAR_MONTH_OUTLINED,
            ft.Icons.CALENDAR_MONTH,
        ),

        (
            "الواجبات",
            ft.Icons.ASSIGNMENT_OUTLINED,
            ft.Icons.ASSIGNMENT,
        ),

        (
            "الأهداف",
            ft.Icons.TODAY_OUTLINED,
            ft.Icons.TODAY,
        ),

        (
            "المعدل",
            ft.Icons.BAR_CHART_OUTLINED,
            ft.Icons.BAR_CHART,
        ),

        (
            "المصاريف",
            ft.Icons.ACCOUNT_BALANCE_WALLET_OUTLINED,
            ft.Icons.ACCOUNT_BALANCE_WALLET,
        ),

        (
            "الملاحظات",
            ft.Icons.NOTE_OUTLINED,
            ft.Icons.NOTE,
        ),

        (
            "الروابط",
            ft.Icons.LINK_OUTLINED,
            ft.Icons.LINK,
        ),
    ]

    # =====================================================
    # عناوين الصفحات
    # =====================================================

    titles = [

        (
            "الرئيسية",
            "نظرة سريعة على يومك الدراسي",
        ),

        (
            "التذكيرات",
            "نظم مواعيدك ولا تنسَ مهامك المهمة",
        ),

        (
            "جدول الحصص",
            "تابع جدولك الدراسي بسهولة",
        ),

        (
            "الواجبات",
            "تابع واجباتك ومواعيد تسليمها",
        ),

        (
            "الأهداف",
            "حوّل أهدافك اليومية إلى إنجازات",
        ),

        (
            "المعدل",
            "تابع نتائجك وتقدمك الدراسي",
        ),

        (
            "المصاريف",
            "تحكم في مصروفاتك وميزانيتك",
        ),

        (
            "الملاحظات",
            "احتفظ بملاحظاتك الدراسية",
        ),

        (
            "الروابط",
            "كل المواقع التي يحتاجها الطالب",
        ),
    ]

    # =====================================================
    # عناصر القائمة
    # =====================================================

    nav_controls = []

    # =====================================================
    # تحديث القائمة
    # =====================================================

    def update_navigation(selected):

        for i, control in enumerate(nav_controls):

            icon = control.content.controls[0]

            text = control.content.controls[1]

            if i == selected:

                control.bgcolor = (
                    "#DCE7FF"
                    if not dark_mode
                    else "#263B63"
                )

                icon.icon = menu_items[i][2]

                icon.color = (
                    "#1D4ED8"
                    if not dark_mode
                    else "#FFFFFF"
                )

                text.color = (
                    "#1D4ED8"
                    if not dark_mode
                    else "#FFFFFF"
                )

            else:

                control.bgcolor = None

                icon.icon = menu_items[i][1]

                icon.color = (
                    "#475467"
                    if not dark_mode
                    else "#CBD5E1"
                )

                text.color = (
                    "#344054"
                    if not dark_mode
                    else "#CBD5E1"
                )

    # =====================================================
    # تغيير الصفحة
    # =====================================================

    def change_page(index):

        if index == 0:

            page_content.content = home_page()

        elif index == 1:

            page_content.content = reminders_page()

        elif index == 2:

            page_content.content = classes_page()

        elif index == 3:

            page_content.content = assignments_page()

        elif index == 4:

            page_content.content = goals_page()

        elif index == 5:

            page_content.content = grades_page()

        elif index == 6:

            page_content.content = expenses_page()

        elif index == 7:

            page_content.content = notes_page()

        elif index == 8:

            page_content.content = links_page()

        page_title.value = titles[index][0]

        page_subtitle.value = titles[index][1]

        status_text.value = (
            f"● {titles[index][0]}"
        )

        navigation.selected_index = index

        update_navigation(index)

        page.update()

    # =====================================================
    # القائمة الجانبية
    # =====================================================

    sidebar_column = ft.Column(
        spacing=6,
        expand=True,
    )

    # =====================================================
    # الشعار
    # =====================================================

    logo = ft.Container(

        content=ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        "🎓",
                        size=26,
                    ),

                    width=50,
                    height=50,

                    alignment=ft.Alignment.CENTER,

                    bgcolor="#2563EB",

                    border_radius=14,
                ),

                ft.Column(
                    [
                        ft.Text(
                            "Student Hub",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color="#172033",
                        ),

                        ft.Text(
                            "مساعد الطالب",
                            size=12,
                            color="#667085",
                        ),
                    ],

                    spacing=1,
                ),
            ],
        ),

        padding=10,
    )

    sidebar_column.controls.append(logo)

    sidebar_column.controls.append(
        ft.Container(
            height=12,
        )
    )

    # =====================================================
    # إنشاء القائمة
    # =====================================================

    for index, item in enumerate(menu_items):

        icon = ft.Icon(
            item[2] if index == 0 else item[1],
            size=21,
            color="#475467",
        )

        text = ft.Text(
            item[0],
            size=14,
            color="#344054",
        )

        button = ft.Container(

            content=ft.Row(
                [
                    icon,
                    text,
                ],

                spacing=14,
            ),

            padding=ft.Padding(
                left=14,
                right=14,
                top=11,
                bottom=11,
            ),

            border_radius=12,

            on_click=lambda e, i=index:
                change_page(i),
        )

        nav_controls.append(button)

        sidebar_column.controls.append(
            button
        )

    # =====================================================
    # فاصل
    # =====================================================

    sidebar_column.controls.append(
        ft.Container(
            height=10,
        )
    )

    sidebar_column.controls.append(
        ft.Divider(
            height=1,
            color="#D0D5DD",
        )
    )

    # =====================================================
    # معلومات التطبيق
    # =====================================================

    sidebar_column.controls.append(

        ft.Container(

            content=ft.Column(
                [
                    ft.Text(
                        "Student Hub",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color="#344054",
                    ),

                    ft.Text(
                        "نظم دراستك • حقق أهدافك",
                        size=11,
                        color="#667085",
                    ),
                ],

                spacing=3,
            ),

            padding=10,
        )
    )

    # =====================================================
    # القائمة الجانبية
    # =====================================================

    sidebar = ft.Container(

        content=sidebar_column,

        width=245,

        padding=12,

        bgcolor="#FFFFFF",
    )

    # =====================================================
    # البحث
    # =====================================================

    search_field = ft.TextField(

        hint_text="بحث سريع...",

        prefix_icon=ft.Icons.SEARCH,

        width=260,

        height=45,

        border_radius=12,

        border_width=1,

        border_color="#D0D5DD",

        filled=True,

        fill_color="#FFFFFF",

        text_style=ft.TextStyle(
            color="#172033",
        ),

        hint_style=ft.TextStyle(
            color="#98A2B3",
        ),
    )

    # =====================================================
    # الوضع الليلي
    # =====================================================

    def toggle_theme(e):

        nonlocal dark_mode

        dark_mode = not dark_mode

        if dark_mode:

            # الخلفية
            page.bgcolor = "#101828"

            # خلفية المحتوى
            background.opacity = 0.10

            # الشريط الجانبي
            sidebar.bgcolor = "#182230"

            # العناوين
            page_title.color = "#FFFFFF"

            page_subtitle.color = "#98A2B3"

            status_text.color = "#98A2B3"

            # البحث
            search_field.fill_color = "#1D2939"

            search_field.border_color = "#344054"

            search_field.text_style = ft.TextStyle(
                color="#FFFFFF",
            )

            search_field.hint_style = ft.TextStyle(
                color="#98A2B3",
            )

            # الزر
            theme_button.icon = (
                ft.Icons.LIGHT_MODE_OUTLINED
            )

            theme_button.icon_color = "#FFFFFF"

        else:

            page.bgcolor = "#EEF2F7"

            # خلفية المحتوى
            background.opacity = 0.18

            sidebar.bgcolor = "#FFFFFF"

            page_title.color = "#172033"

            page_subtitle.color = "#667085"

            status_text.color = "#667085"

            search_field.fill_color = "#FFFFFF"

            search_field.border_color = "#D0D5DD"

            search_field.text_style = ft.TextStyle(
                color="#172033",
            )

            search_field.hint_style = ft.TextStyle(
                color="#98A2B3",
            )

            theme_button.icon = (
                ft.Icons.DARK_MODE_OUTLINED
            )

            theme_button.icon_color = "#344054"

        update_navigation(
            navigation.selected_index
        )

        page.update()

    theme_button.on_click = toggle_theme

    # =====================================================
    # الشريط العلوي
    # =====================================================

    topbar = ft.Container(

        content=ft.Row(
            [
                ft.Column(
                    [
                        page_title,
                        page_subtitle,
                    ],

                    spacing=2,

                    expand=True,
                ),

                search_field,

                theme_button,

                ft.IconButton(
                    icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                    tooltip="الإشعارات",
                    icon_color="#475467",
                ),

                ft.Container(
                    content=ft.Text(
                        "👤",
                        size=20,
                    ),

                    width=42,

                    height=42,

                    alignment=ft.Alignment.CENTER,

                    bgcolor="#E8EEFF",

                    border_radius=12,
                ),
            ],

            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),

        padding=ft.Padding(
            left=25,
            right=25,
            top=18,
            bottom=18,
        ),
    )

    # =====================================================
    # شريط الحالة
    # =====================================================

    bottom_status = ft.Container(

        content=ft.Row(
            [
                ft.Text(
                    "🎓 Student Hub",
                    size=12,
                    color="#667085",
                ),

                ft.Container(
                    expand=True,
                ),

                status_text,
            ]
        ),

        padding=ft.Padding(
            left=25,
            right=25,
            top=8,
            bottom=8,
        ),
    )

    # =====================================================
    # التخطيط الرئيسي
    # =====================================================

    navigation = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.NONE,
        extended=False,
        width=0,
    )

    # =====================================================
    # الواجهة الرئيسية
    # =====================================================

    page.add(

        ft.Row(
            [
                sidebar,

                ft.VerticalDivider(
                    width=1,
                    color="#D0D5DD",
                ),

                ft.Column(
                    [
                        topbar,

                        ft.Divider(
                            height=1,
                            color="#D0D5DD",
                        ),

                        content,

                        bottom_status,
                    ],

                    expand=True,

                    spacing=0,
                ),
            ],

            expand=True,

            spacing=0,
        )
    )

    # =====================================================
    # فتح الرئيسية
    # =====================================================

    update_navigation(0)

    change_page(0)


# =========================================================
# تشغيل البرنامج
# =========================================================

ft.run(main)
