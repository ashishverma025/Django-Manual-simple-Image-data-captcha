from captcha import getCaptcha

def MyView():
    text, captchaImg = getCaptcha()
    request.session['captchaCode'] = text  # SET CODE IN TO SESSION
    return render_to_response('mytemplate.html', locals())

def getCaptcha_ajax(request):
    # CAPTCHA GET START
    from getlead.captcha import getCaptcha
    text, captchaImg = getCaptcha()
    request.session['captchaCode'] = text  # SET CODE IN TO SESSION
    # CAPTCHA GET END
    template_name = 'captcha/captchaAjaxTemplate.html'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

