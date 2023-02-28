from django.shortcuts import render

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden

from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from linebot import LineBotApi, WebhookParser

from linebot.exceptions import InvalidSignatureError, LineBotApiError

from linebot.models import MessageEvent, TextSendMessage

#LINE_CHANNEL_ACCESS_TOKEN、LINE_CHANNEL_SECRET設定

line_bot_api = LineBotApi('qcHTcLOugkdGwCDRK/e8SJtMhb+gAhGd9/0cXc8V4kK1Ronk6SSrbqKwITzVyLAwSsHPiCaPtQnwqFEQOkNT9VaoGxYr/rdrgC0TKIfqBnvExqb/P+gkf+4DgB4Xj0m4zmdXXcgqt87IO3ox/lyk9gdB04t89/1O/w1cDnyilFU=')

parser = WebhookParser('e3ce636500600f51ca460ab14d14567a')

@csrf_exempt
def callback(request):
    if request.method == 'POST':

    #接收訊息

        signature = request.META['HTTP_X_LINE_SIGNATURE']

        body = request.body.decode('utf-8')

    try:

        events = parser.parse(body, signature)

        print(events)

    except InvalidSignatureError:

        return  HttpResponseForbidden()

    except LineBotApiError:

        return HttpResponseBadRequest()

    #回復訊息

    for event in events:

        if isinstance(event, MessageEvent):#觸發事件

            line_bot_api.reply_message(#回復訊息

            event.reply_token,

            TextSendMessage(text=event.message.text))

            print("check,",event)

            return HttpResponse()

        else:

            return HttpResponseBadRequest()