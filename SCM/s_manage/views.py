from django.shortcuts import render
from django.template import TemplateDoesNotExist

# Create your views here.

from s_manage.View.StudentView import StudentRegistrationSerializer

from django.template.loader import render_to_string


from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response

# def select_template(template_name_list, using=None):
#     """
#     Load and return a template for one of the given names.

#     Try names in order and return the first template found.

#     Raise TemplateDoesNotExist if no such template exists.
#     """
#     if isinstance(template_name_list, str):
#         raise TypeError(
#             "select_template() takes an iterable of template names but got a "
#             "string: %r. Use get_template() if you want to load a single "
#             "template by name." % template_name_list
#         )

#     chain = []
#     engines = _engine_list(using)
#     for template_name in template_name_list:
#         for engine in engines:
#             try:
#                 return engine.get_template(template_name)
#             except TemplateDoesNotExist as e:
#                 chain.append(e)

#     if template_name_list:
#         raise TemplateDoesNotExist(", ".join(template_name_list), chain=chain)
#     else:
#         raise TemplateDoesNotExist("No template names provided")

# def render_to_string(template_name, context=None, request=None, using=None):
#     """
#     Load a template and render it with a context. Return a string.

#     template_name may be a string or a list of strings.
#     """
#     if isinstance(template_name, (list, tuple)):
#         template = select_template(template_name, using=using)
#     else:
#         template = get_template(template_name, using=using)
#     return template.render(context, request)

class EmailAPI(APIView):
    
    def post(self, request):
        subject = self.request.GET.get('subject')
        txt_ = self.request.GET.get('text')
        html_ = self.request.GET.get('html')
        msg_html = render_to_string(template_name='email3.html'),
        recipient_list = self.request.GET.get('recipient_list')
        from_email = "vikashbaraiya786@gmail.com"
        # breakpoint()
        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)
        elif html_ is not None and txt_ is not None:
            return Response({'msg': 'You can either use HTML or Text.'}, status=200)
        elif html_ is None and txt_ is None:
            return Response({'msg': 'Either HTML or Text is required.'}, status=200)
        elif recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        elif subject is None:
            return Response({'msg': 'Subject required.'}, status=200)
        else:
            sent_mail = send_mail(
                subject,
                txt_,
                from_email,
                recipient_list=['vikashbaraiya786@gmail.com'],
                html_message="".join(msg_html),
                fail_silently=False,
            )
           
            return Response({'msg': sent_mail}, status=200)