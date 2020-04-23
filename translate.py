from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'_$_7e76', u'e', u're', u'r', u'vsd', u't', u'link', u'_$_9566'])
@Js
def PyJsHoisted_r_(n, PyJsArg_646566_, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'def':PyJsArg_646566_, u'n':n}, var)
    var.registers([u'def', u'n'])
    def PyJs_LONG_6_(var=var):
        return (var.get(u'String').callprop(var.get(u'_$_7e76').get(u'4'), (var.get(u'n') if ((Js(91.0) if (var.get(u'n')<var.get(u'_$_7e76').get(u'2')) else Js(123.0))>var.put(u'n', (var.get(u'n').callprop(var.get(u'_$_7e76').get(u'3'))+Js(13.0)))) else (var.get(u'n')-Js(26.0)))) if var.put(u'def',Js(var.get(u'def').to_number())+Js(1)) else var.get(u'n').callprop(var.get(u'_$_7e76').get(u'5'), JsRegExp(u'/[a-zA-Z]/g'), var.get(u'r')))
    return PyJs_LONG_6_()
PyJsHoisted_r_.func_name = u'r'
var.put(u'r', PyJsHoisted_r_)
@Js
def PyJsHoisted_link_(hashedurl, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'hashedurl':hashedurl}, var)
    var.registers([u'ved', u'od', u'sed', u'hashedurl'])
    var.put(u'ved', var.get(u're')(var.get(u'hashedurl'), var.get(u't')))
    var.put(u'od', var.get(u'vsd').callprop(u'd', ((Js(u'')+var.get(u'ved'))+Js(u''))))
    var.put(u'sed', var.get(u're')(((Js(u'')+var.get(u'od'))+Js(u'')), var.get(u'e')))
    return var.get(u'sed')
PyJsHoisted_link_.func_name = u'link'
var.put(u'link', PyJsHoisted_link_)
Js(u'use strict')
var.put(u'_$_9566', Js([Js(u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='), Js(u''), Js(u'_utf8_encode'), Js(u'charCodeAt'), Js(u'charAt'), Js(u'_keyStr'), Js(u'length'), Js(u'replace'), Js(u'indexOf'), Js(u'fromCharCode'), Js(u'_utf8_decode'), Js(u'\n')]))
@Js
def PyJs_anonymous_1_(data, this, arguments, var=var):
    var = Scope({u'this':this, u'data':data, u'arguments':arguments}, var)
    var.registers([u'dword2', u'fillTranslate', u'i', u'knobTranslate', u'value', u'aStatedRank', u'offset', u'normalized_images', u'data', u'ARByte'])
    var.put(u'offset', var.get(u'_$_9566').get(u'1'))
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    var.put(u'i', Js(0.0))
    var.put(u'data', var.get(u'vsd').callprop(var.get(u'_$_9566').get(u'2'), var.get(u'data')))
    #for JS loop
    
    while (var.get(u'i')<var.get(u'data').get(var.get(u'_$_9566').get(u'6'))):
        var.put(u'dword2', var.get(u'data').callprop(var.get(u'_$_9566').get(u'3'), (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))))
        var.put(u'aStatedRank', var.get(u'data').callprop(var.get(u'_$_9566').get(u'3'), (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))))
        var.put(u'normalized_images', var.get(u'data').callprop(var.get(u'_$_9566').get(u'3'), (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))))
        var.put(u'ARByte', (var.get(u'dword2')>>Js(2.0)))
        var.put(u'value', (((var.get(u'dword2')&Js(3.0))<<Js(4.0))|(var.get(u'aStatedRank')>>Js(4.0))))
        var.put(u'knobTranslate', (((var.get(u'aStatedRank')&Js(15.0))<<Js(2.0))|(var.get(u'normalized_images')>>Js(6.0))))
        var.put(u'fillTranslate', (var.get(u'normalized_images')&Js(63.0)))
        if var.get(u'isNaN')(var.get(u'aStatedRank')):
            var.put(u'knobTranslate', var.put(u'fillTranslate', Js(64.0)))
        else:
            if var.get(u'isNaN')(var.get(u'normalized_images')):
                var.put(u'fillTranslate', Js(64.0))
        def PyJs_LONG_2_(var=var):
            return ((((var.get(u'offset')+var.get(u"this").get(var.get(u'_$_9566').get(u'5')).callprop(var.get(u'_$_9566').get(u'4'), var.get(u'ARByte')))+var.get(u"this").get(var.get(u'_$_9566').get(u'5')).callprop(var.get(u'_$_9566').get(u'4'), var.get(u'value')))+var.get(u"this").get(var.get(u'_$_9566').get(u'5')).callprop(var.get(u'_$_9566').get(u'4'), var.get(u'knobTranslate')))+var.get(u"this").get(var.get(u'_$_9566').get(u'5')).callprop(var.get(u'_$_9566').get(u'4'), var.get(u'fillTranslate')))
        var.put(u'offset', PyJs_LONG_2_())
    
    return var.get(u'offset')
PyJs_anonymous_1_._set_name(u'anonymous')
@Js
def PyJs_anonymous_3_(data, this, arguments, var=var):
    var = Scope({u'this':this, u'data':data, u'arguments':arguments}, var)
    var.registers([u'opCipher', u'val', u'expectedSecureOpts', u'i', u'elem', u'start', u'_0x64DD', u'sextet2', u'sextet1', u'data'])
    var.put(u'val', var.get(u'_$_9566').get(u'1'))
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    var.put(u'i', Js(0.0))
    var.put(u'data', var.get(u'data').callprop(var.get(u'_$_9566').get(u'7'), JsRegExp(u'/[^A-Za-z0-9\\+\\/=]/g'), var.get(u'_$_9566').get(u'1')))
    #for JS loop
    
    while (var.get(u'i')<var.get(u'data').get(var.get(u'_$_9566').get(u'6'))):
        var.put(u'sextet1', var.get(u"this").get(var.get(u'_$_9566').get(u'5')).callprop(var.get(u'_$_9566').get(u'8'), var.get(u'data').callprop(var.get(u'_$_9566').get(u'4'), (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1)))))
        var.put(u'sextet2', var.get(u"this").get(var.get(u'_$_9566').get(u'5')).callprop(var.get(u'_$_9566').get(u'8'), var.get(u'data').callprop(var.get(u'_$_9566').get(u'4'), (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1)))))
        var.put(u'_0x64DD', var.get(u"this").get(var.get(u'_$_9566').get(u'5')).callprop(var.get(u'_$_9566').get(u'8'), var.get(u'data').callprop(var.get(u'_$_9566').get(u'4'), (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1)))))
        var.put(u'opCipher', var.get(u"this").get(var.get(u'_$_9566').get(u'5')).callprop(var.get(u'_$_9566').get(u'8'), var.get(u'data').callprop(var.get(u'_$_9566').get(u'4'), (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1)))))
        var.put(u'elem', ((var.get(u'sextet1')<<Js(2.0))|(var.get(u'sextet2')>>Js(4.0))))
        var.put(u'start', (((var.get(u'sextet2')&Js(15.0))<<Js(4.0))|(var.get(u'_0x64DD')>>Js(2.0))))
        var.put(u'expectedSecureOpts', (((var.get(u'_0x64DD')&Js(3.0))<<Js(6.0))|var.get(u'opCipher')))
        var.put(u'val', (var.get(u'val')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), var.get(u'elem'))))
        if (var.get(u'_0x64DD')!=Js(64.0)):
            var.put(u'val', (var.get(u'val')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), var.get(u'start'))))
        if (var.get(u'opCipher')!=Js(64.0)):
            var.put(u'val', (var.get(u'val')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), var.get(u'expectedSecureOpts'))))
    
    var.put(u'val', var.get(u'vsd').callprop(var.get(u'_$_9566').get(u'10'), var.get(u'val')))
    return var.get(u'val')
PyJs_anonymous_3_._set_name(u'anonymous')
@Js
def PyJs_anonymous_4_(PyJsArg_504c243432_, this, arguments, var=var):
    var = Scope({u'this':this, u'PL$42':PyJsArg_504c243432_, u'arguments':arguments}, var)
    var.registers([u'PL$41', u'c', u'PL$42', u'utftext'])
    var.put(u'PL$42', var.get(u'PL$42').callprop(var.get(u'_$_9566').get(u'7'), JsRegExp(u'/\\r\\n/g'), var.get(u'_$_9566').get(u'11')))
    var.put(u'utftext', var.get(u'_$_9566').get(u'1'))
    var.put(u'PL$41', Js(0.0))
    #for JS loop
    
    while (var.get(u'PL$41')<var.get(u'PL$42').get(var.get(u'_$_9566').get(u'6'))):
        try:
            var.put(u'c', var.get(u'PL$42').callprop(var.get(u'_$_9566').get(u'3'), var.get(u'PL$41')))
            if (var.get(u'c')<Js(128.0)):
                var.put(u'utftext', (var.get(u'utftext')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), var.get(u'c'))))
            else:
                if ((var.get(u'c')>Js(127.0)) and (var.get(u'c')<Js(2048.0))):
                    var.put(u'utftext', (var.get(u'utftext')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), ((var.get(u'c')>>Js(6.0))|Js(192.0)))))
                    var.put(u'utftext', (var.get(u'utftext')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), ((var.get(u'c')&Js(63.0))|Js(128.0)))))
                else:
                    var.put(u'utftext', (var.get(u'utftext')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), ((var.get(u'c')>>Js(12.0))|Js(224.0)))))
                    var.put(u'utftext', (var.get(u'utftext')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), (((var.get(u'c')>>Js(6.0))&Js(63.0))|Js(128.0)))))
                    var.put(u'utftext', (var.get(u'utftext')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), ((var.get(u'c')&Js(63.0))|Js(128.0)))))
        finally:
                (var.put(u'PL$41',Js(var.get(u'PL$41').to_number())+Js(1))-Js(1))
    return var.get(u'utftext')
PyJs_anonymous_4_._set_name(u'anonymous')
@Js
def PyJs_anonymous_5_(view, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'view':view}, var)
    var.registers([u'c', u'view', u'string', u'offset'])
    var.put(u'string', var.get(u'_$_9566').get(u'1'))
    var.put(u'offset', Js(0.0))
    var.put(u'c', var.put(u'c1', var.put(u'c2', Js(0.0))))
    #for JS loop
    
    while (var.get(u'offset')<var.get(u'view').get(var.get(u'_$_9566').get(u'6'))):
        var.put(u'c', var.get(u'view').callprop(var.get(u'_$_9566').get(u'3'), var.get(u'offset')))
        if (var.get(u'c')<Js(128.0)):
            var.put(u'string', (var.get(u'string')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), var.get(u'c'))))
            (var.put(u'offset',Js(var.get(u'offset').to_number())+Js(1))-Js(1))
        else:
            if ((var.get(u'c')>Js(191.0)) and (var.get(u'c')<Js(224.0))):
                var.put(u'c2', var.get(u'view').callprop(var.get(u'_$_9566').get(u'3'), (var.get(u'offset')+Js(1.0))))
                var.put(u'string', (var.get(u'string')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), (((var.get(u'c')&Js(31.0))<<Js(6.0))|(var.get(u'c2')&Js(63.0))))))
                var.put(u'offset', (var.get(u'offset')+Js(2.0)))
            else:
                var.put(u'c2', var.get(u'view').callprop(var.get(u'_$_9566').get(u'3'), (var.get(u'offset')+Js(1.0))))
                var.put(u'c3', var.get(u'view').callprop(var.get(u'_$_9566').get(u'3'), (var.get(u'offset')+Js(2.0))))
                var.put(u'string', (var.get(u'string')+var.get(u'String').callprop(var.get(u'_$_9566').get(u'9'), ((((var.get(u'c')&Js(15.0))<<Js(12.0))|((var.get(u'c2')&Js(63.0))<<Js(6.0)))|(var.get(u'c3')&Js(63.0))))))
                var.put(u'offset', (var.get(u'offset')+Js(3.0)))
    
    return var.get(u'string')
PyJs_anonymous_5_._set_name(u'anonymous')
PyJs_Object_0_ = Js({u'_keyStr':var.get(u'_$_9566').get(u'0'),u'encode':PyJs_anonymous_1_,u'd':PyJs_anonymous_3_,u'_utf8_encode':PyJs_anonymous_4_,u'_utf8_decode':PyJs_anonymous_5_})
var.put(u'vsd', PyJs_Object_0_)
var.put(u'_$_7e76', Js([Js(u'+10'), Js(u'+8'), Js(u'['), Js(u'charCodeAt'), Js(u'fromCharCode'), Js(u'replace'), Js(u''), Js(u'length')]))
var.put(u't', var.get(u'_$_7e76').get(u'0'))
var.put(u'e', var.get(u'_$_7e76').get(u'1'))
pass
@Js
def PyJs_anonymous_7_(p, actual, this, arguments, var=var):
    var = Scope({u'this':this, u'p':p, u'actual':actual, u'arguments':arguments}, var)
    var.registers([u'a', u'note', u'sum', u'actual', u'p'])
    var.put(u'sum', var.get(u'_$_7e76').get(u'6'))
    var.put(u'a', Js(0.0))
    #for JS loop
    
    while (var.get(u'a')<var.get(u'p').get(var.get(u'_$_7e76').get(u'7'))):
        try:
            var.put(u'note', var.get(u'p').callprop(var.get(u'_$_7e76').get(u'3'), var.get(u'a')))
            if ((var.get(u'note')>=Js(97.0)) and (var.get(u'note')<=Js(122.0))):
                var.put(u'sum', (var.get(u'sum')+var.get(u'String').callprop(var.get(u'_$_7e76').get(u'4'), (((((var.get(u'note')-Js(97.0))-var.get(u'actual'))+Js(26.0))%Js(26.0))+Js(97.0)))))
            else:
                if ((var.get(u'note')>=Js(65.0)) and (var.get(u'note')<=Js(90.0))):
                    var.put(u'sum', (var.get(u'sum')+var.get(u'String').callprop(var.get(u'_$_7e76').get(u'4'), (((((var.get(u'note')-Js(65.0))-var.get(u'actual'))+Js(26.0))%Js(26.0))+Js(65.0)))))
                else:
                    var.put(u'sum', (var.get(u'sum')+var.get(u'String').callprop(var.get(u'_$_7e76').get(u'4'), var.get(u'note'))))
        finally:
                (var.put(u'a',Js(var.get(u'a').to_number())+Js(1))-Js(1))
    return var.get(u'sum')
PyJs_anonymous_7_._set_name(u'anonymous')
var.put(u're', PyJs_anonymous_7_)
pass
pass
