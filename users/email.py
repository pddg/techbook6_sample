from djoser.email import ActivationEmail


class MyActivationEmail(ActivationEmail):

    def get_context_data(self):
        context = super(SaffronActivationEmail, self).get_context_data()
        context['techbook_team'] = "あくあたん工房"
        return context
