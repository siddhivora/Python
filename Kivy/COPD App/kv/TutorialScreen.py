<TutorialScreen>:
    BoxLayout:
        Label:
            text: 'Tutorial'
        Button:
            text: 'Back to Patient'
            on_press: root.manager.current = 'patient'