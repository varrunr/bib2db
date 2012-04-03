# This file is part of the Basilic system
# Copyright (C) 2004  Gilles Debunne (Gilles.Debunne@imag.fr)
# Version 1.5.14, packaged on May 2, 2007.
# 
# http://artis.imag.fr/Software/Basilic
# 
# Basilic  is  free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2 of the License,
# or (at your option) any later version.
# 
# Basilic  is  distributed  in the hope that it will be useful, but
# WITHOUT  ANY  WARRANTY ; without  even  the  implied  warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Basilic; if not, write to the Free Software Foundation
# Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pyxdkbibtex

def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class vectorvaluepart(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorvaluepart, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorvaluepart, name)
    def __repr__(self):
        return "<C std::vector<(xdkbib::ValuePart)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, vectorvaluepart, 'this', _pyxdkbibtex.new_vectorvaluepart(*args))
        _swig_setattr(self, vectorvaluepart, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.vectorvaluepart___len__(*args)
    def clear(*args): return _pyxdkbibtex.vectorvaluepart_clear(*args)
    def append(*args): return _pyxdkbibtex.vectorvaluepart_append(*args)
    def __nonzero__(*args): return _pyxdkbibtex.vectorvaluepart___nonzero__(*args)
    def pop(*args): return _pyxdkbibtex.vectorvaluepart_pop(*args)
    def __getitem__(*args): return _pyxdkbibtex.vectorvaluepart___getitem__(*args)
    def __getslice__(*args): return _pyxdkbibtex.vectorvaluepart___getslice__(*args)
    def __setitem__(*args): return _pyxdkbibtex.vectorvaluepart___setitem__(*args)
    def __setslice__(*args): return _pyxdkbibtex.vectorvaluepart___setslice__(*args)
    def __delitem__(*args): return _pyxdkbibtex.vectorvaluepart___delitem__(*args)
    def __delslice__(*args): return _pyxdkbibtex.vectorvaluepart___delslice__(*args)
    def __str__(*args): return _pyxdkbibtex.vectorvaluepart___str__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_vectorvaluepart):
        try:
            if self.thisown: destroy(self)
        except: pass

class vectorvaluepartPtr(vectorvaluepart):
    def __init__(self, this):
        _swig_setattr(self, vectorvaluepart, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, vectorvaluepart, 'thisown', 0)
        _swig_setattr(self, vectorvaluepart,self.__class__,vectorvaluepart)
_pyxdkbibtex.vectorvaluepart_swigregister(vectorvaluepartPtr)

class mapentry(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mapentry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mapentry, name)
    def __repr__(self):
        return "<C std::map<(std::string,xdkbib::Field)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, mapentry, 'this', _pyxdkbibtex.new_mapentry(*args))
        _swig_setattr(self, mapentry, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.mapentry___len__(*args)
    def clear(*args): return _pyxdkbibtex.mapentry_clear(*args)
    def __nonzero__(*args): return _pyxdkbibtex.mapentry___nonzero__(*args)
    def __getitem__(*args): return _pyxdkbibtex.mapentry___getitem__(*args)
    def __setitem__(*args): return _pyxdkbibtex.mapentry___setitem__(*args)
    def __delitem__(*args): return _pyxdkbibtex.mapentry___delitem__(*args)
    def has_key(*args): return _pyxdkbibtex.mapentry_has_key(*args)
    def keys(*args): return _pyxdkbibtex.mapentry_keys(*args)
    def values(*args): return _pyxdkbibtex.mapentry_values(*args)
    def items(*args): return _pyxdkbibtex.mapentry_items(*args)
    def __contains__(*args): return _pyxdkbibtex.mapentry___contains__(*args)
    def __iter__(*args): return _pyxdkbibtex.mapentry___iter__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_mapentry):
        try:
            if self.thisown: destroy(self)
        except: pass

class mapentryPtr(mapentry):
    def __init__(self, this):
        _swig_setattr(self, mapentry, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mapentry, 'thisown', 0)
        _swig_setattr(self, mapentry,self.__class__,mapentry)
_pyxdkbibtex.mapentry_swigregister(mapentryPtr)

class vectorvectorvaluepart(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorvectorvaluepart, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorvectorvaluepart, name)
    def __repr__(self):
        return "<C std::vector<(std::vector<(xdkbib::ValuePart)>)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, vectorvectorvaluepart, 'this', _pyxdkbibtex.new_vectorvectorvaluepart(*args))
        _swig_setattr(self, vectorvectorvaluepart, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.vectorvectorvaluepart___len__(*args)
    def clear(*args): return _pyxdkbibtex.vectorvectorvaluepart_clear(*args)
    def append(*args): return _pyxdkbibtex.vectorvectorvaluepart_append(*args)
    def __nonzero__(*args): return _pyxdkbibtex.vectorvectorvaluepart___nonzero__(*args)
    def pop(*args): return _pyxdkbibtex.vectorvectorvaluepart_pop(*args)
    def __getitem__(*args): return _pyxdkbibtex.vectorvectorvaluepart___getitem__(*args)
    def __getslice__(*args): return _pyxdkbibtex.vectorvectorvaluepart___getslice__(*args)
    def __setitem__(*args): return _pyxdkbibtex.vectorvectorvaluepart___setitem__(*args)
    def __setslice__(*args): return _pyxdkbibtex.vectorvectorvaluepart___setslice__(*args)
    def __delitem__(*args): return _pyxdkbibtex.vectorvectorvaluepart___delitem__(*args)
    def __delslice__(*args): return _pyxdkbibtex.vectorvectorvaluepart___delslice__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_vectorvectorvaluepart):
        try:
            if self.thisown: destroy(self)
        except: pass

class vectorvectorvaluepartPtr(vectorvectorvaluepart):
    def __init__(self, this):
        _swig_setattr(self, vectorvectorvaluepart, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, vectorvectorvaluepart, 'thisown', 0)
        _swig_setattr(self, vectorvectorvaluepart,self.__class__,vectorvectorvaluepart)
_pyxdkbibtex.vectorvectorvaluepart_swigregister(vectorvectorvaluepartPtr)

class vectorfileentry(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorfileentry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorfileentry, name)
    def __repr__(self):
        return "<C std::vector<(xdkbib::FileEntry)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, vectorfileentry, 'this', _pyxdkbibtex.new_vectorfileentry(*args))
        _swig_setattr(self, vectorfileentry, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.vectorfileentry___len__(*args)
    def clear(*args): return _pyxdkbibtex.vectorfileentry_clear(*args)
    def append(*args): return _pyxdkbibtex.vectorfileentry_append(*args)
    def __nonzero__(*args): return _pyxdkbibtex.vectorfileentry___nonzero__(*args)
    def pop(*args): return _pyxdkbibtex.vectorfileentry_pop(*args)
    def __getitem__(*args): return _pyxdkbibtex.vectorfileentry___getitem__(*args)
    def __getslice__(*args): return _pyxdkbibtex.vectorfileentry___getslice__(*args)
    def __setitem__(*args): return _pyxdkbibtex.vectorfileentry___setitem__(*args)
    def __setslice__(*args): return _pyxdkbibtex.vectorfileentry___setslice__(*args)
    def __delitem__(*args): return _pyxdkbibtex.vectorfileentry___delitem__(*args)
    def __delslice__(*args): return _pyxdkbibtex.vectorfileentry___delslice__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_vectorfileentry):
        try:
            if self.thisown: destroy(self)
        except: pass

class vectorfileentryPtr(vectorfileentry):
    def __init__(self, this):
        _swig_setattr(self, vectorfileentry, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, vectorfileentry, 'thisown', 0)
        _swig_setattr(self, vectorfileentry,self.__class__,vectorfileentry)
_pyxdkbibtex.vectorfileentry_swigregister(vectorfileentryPtr)

class mapvectorvaluepart(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mapvectorvaluepart, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mapvectorvaluepart, name)
    def __repr__(self):
        return "<C std::map<(std::string,std::vector<(xdkbib::ValuePart)>)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, mapvectorvaluepart, 'this', _pyxdkbibtex.new_mapvectorvaluepart(*args))
        _swig_setattr(self, mapvectorvaluepart, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.mapvectorvaluepart___len__(*args)
    def clear(*args): return _pyxdkbibtex.mapvectorvaluepart_clear(*args)
    def __nonzero__(*args): return _pyxdkbibtex.mapvectorvaluepart___nonzero__(*args)
    def __getitem__(*args): return _pyxdkbibtex.mapvectorvaluepart___getitem__(*args)
    def __setitem__(*args): return _pyxdkbibtex.mapvectorvaluepart___setitem__(*args)
    def __delitem__(*args): return _pyxdkbibtex.mapvectorvaluepart___delitem__(*args)
    def has_key(*args): return _pyxdkbibtex.mapvectorvaluepart_has_key(*args)
    def keys(*args): return _pyxdkbibtex.mapvectorvaluepart_keys(*args)
    def values(*args): return _pyxdkbibtex.mapvectorvaluepart_values(*args)
    def items(*args): return _pyxdkbibtex.mapvectorvaluepart_items(*args)
    def __contains__(*args): return _pyxdkbibtex.mapvectorvaluepart___contains__(*args)
    def __iter__(*args): return _pyxdkbibtex.mapvectorvaluepart___iter__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_mapvectorvaluepart):
        try:
            if self.thisown: destroy(self)
        except: pass

class mapvectorvaluepartPtr(mapvectorvaluepart):
    def __init__(self, this):
        _swig_setattr(self, mapvectorvaluepart, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mapvectorvaluepart, 'thisown', 0)
        _swig_setattr(self, mapvectorvaluepart,self.__class__,mapvectorvaluepart)
_pyxdkbibtex.mapvectorvaluepart_swigregister(mapvectorvaluepartPtr)

class vectorstring(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorstring, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorstring, name)
    def __repr__(self):
        return "<C std::vector<(std::string)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, vectorstring, 'this', _pyxdkbibtex.new_vectorstring(*args))
        _swig_setattr(self, vectorstring, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.vectorstring___len__(*args)
    def __nonzero__(*args): return _pyxdkbibtex.vectorstring___nonzero__(*args)
    def clear(*args): return _pyxdkbibtex.vectorstring_clear(*args)
    def append(*args): return _pyxdkbibtex.vectorstring_append(*args)
    def pop(*args): return _pyxdkbibtex.vectorstring_pop(*args)
    def __getitem__(*args): return _pyxdkbibtex.vectorstring___getitem__(*args)
    def __getslice__(*args): return _pyxdkbibtex.vectorstring___getslice__(*args)
    def __setitem__(*args): return _pyxdkbibtex.vectorstring___setitem__(*args)
    def __setslice__(*args): return _pyxdkbibtex.vectorstring___setslice__(*args)
    def __delitem__(*args): return _pyxdkbibtex.vectorstring___delitem__(*args)
    def __delslice__(*args): return _pyxdkbibtex.vectorstring___delslice__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_vectorstring):
        try:
            if self.thisown: destroy(self)
        except: pass

class vectorstringPtr(vectorstring):
    def __init__(self, this):
        _swig_setattr(self, vectorstring, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, vectorstring, 'thisown', 0)
        _swig_setattr(self, vectorstring,self.__class__,vectorstring)
_pyxdkbibtex.vectorstring_swigregister(vectorstringPtr)

class vectorword(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorword, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorword, name)
    def __repr__(self):
        return "<C std::vector<(p.xdkbib::Word)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, vectorword, 'this', _pyxdkbibtex.new_vectorword(*args))
        _swig_setattr(self, vectorword, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.vectorword___len__(*args)
    def clear(*args): return _pyxdkbibtex.vectorword_clear(*args)
    def append(*args): return _pyxdkbibtex.vectorword_append(*args)
    def __nonzero__(*args): return _pyxdkbibtex.vectorword___nonzero__(*args)
    def pop(*args): return _pyxdkbibtex.vectorword_pop(*args)
    def __getitem__(*args): return _pyxdkbibtex.vectorword___getitem__(*args)
    def __getslice__(*args): return _pyxdkbibtex.vectorword___getslice__(*args)
    def __setitem__(*args): return _pyxdkbibtex.vectorword___setitem__(*args)
    def __setslice__(*args): return _pyxdkbibtex.vectorword___setslice__(*args)
    def __delitem__(*args): return _pyxdkbibtex.vectorword___delitem__(*args)
    def __delslice__(*args): return _pyxdkbibtex.vectorword___delslice__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_vectorword):
        try:
            if self.thisown: destroy(self)
        except: pass

class vectorwordPtr(vectorword):
    def __init__(self, this):
        _swig_setattr(self, vectorword, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, vectorword, 'thisown', 0)
        _swig_setattr(self, vectorword,self.__class__,vectorword)
_pyxdkbibtex.vectorword_swigregister(vectorwordPtr)

class vectorletter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorletter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorletter, name)
    def __repr__(self):
        return "<C std::vector<(p.xdkbib::Letter)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, vectorletter, 'this', _pyxdkbibtex.new_vectorletter(*args))
        _swig_setattr(self, vectorletter, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.vectorletter___len__(*args)
    def clear(*args): return _pyxdkbibtex.vectorletter_clear(*args)
    def append(*args): return _pyxdkbibtex.vectorletter_append(*args)
    def __nonzero__(*args): return _pyxdkbibtex.vectorletter___nonzero__(*args)
    def pop(*args): return _pyxdkbibtex.vectorletter_pop(*args)
    def __getitem__(*args): return _pyxdkbibtex.vectorletter___getitem__(*args)
    def __getslice__(*args): return _pyxdkbibtex.vectorletter___getslice__(*args)
    def __setitem__(*args): return _pyxdkbibtex.vectorletter___setitem__(*args)
    def __setslice__(*args): return _pyxdkbibtex.vectorletter___setslice__(*args)
    def __delitem__(*args): return _pyxdkbibtex.vectorletter___delitem__(*args)
    def __delslice__(*args): return _pyxdkbibtex.vectorletter___delslice__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_vectorletter):
        try:
            if self.thisown: destroy(self)
        except: pass

class vectorletterPtr(vectorletter):
    def __init__(self, this):
        _swig_setattr(self, vectorletter, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, vectorletter, 'thisown', 0)
        _swig_setattr(self, vectorletter,self.__class__,vectorletter)
_pyxdkbibtex.vectorletter_swigregister(vectorletterPtr)

class vectorauthor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorauthor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorauthor, name)
    def __repr__(self):
        return "<C std::vector<(xdkbib::Author)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, vectorauthor, 'this', _pyxdkbibtex.new_vectorauthor(*args))
        _swig_setattr(self, vectorauthor, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.vectorauthor___len__(*args)
    def clear(*args): return _pyxdkbibtex.vectorauthor_clear(*args)
    def append(*args): return _pyxdkbibtex.vectorauthor_append(*args)
    def __nonzero__(*args): return _pyxdkbibtex.vectorauthor___nonzero__(*args)
    def pop(*args): return _pyxdkbibtex.vectorauthor_pop(*args)
    def __getitem__(*args): return _pyxdkbibtex.vectorauthor___getitem__(*args)
    def __getslice__(*args): return _pyxdkbibtex.vectorauthor___getslice__(*args)
    def __setitem__(*args): return _pyxdkbibtex.vectorauthor___setitem__(*args)
    def __setslice__(*args): return _pyxdkbibtex.vectorauthor___setslice__(*args)
    def __delitem__(*args): return _pyxdkbibtex.vectorauthor___delitem__(*args)
    def __delslice__(*args): return _pyxdkbibtex.vectorauthor___delslice__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_vectorauthor):
        try:
            if self.thisown: destroy(self)
        except: pass

class vectorauthorPtr(vectorauthor):
    def __init__(self, this):
        _swig_setattr(self, vectorauthor, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, vectorauthor, 'thisown', 0)
        _swig_setattr(self, vectorauthor,self.__class__,vectorauthor)
_pyxdkbibtex.vectorauthor_swigregister(vectorauthorPtr)

class mappairstringstringstring(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mappairstringstringstring, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mappairstringstringstring, name)
    def __repr__(self):
        return "<C std::map<(std::pair<(std::string,std::string)>,std::string)> instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, mappairstringstringstring, 'this', _pyxdkbibtex.new_mappairstringstringstring(*args))
        _swig_setattr(self, mappairstringstringstring, 'thisown', 1)
    def __len__(*args): return _pyxdkbibtex.mappairstringstringstring___len__(*args)
    def clear(*args): return _pyxdkbibtex.mappairstringstringstring_clear(*args)
    def __nonzero__(*args): return _pyxdkbibtex.mappairstringstringstring___nonzero__(*args)
    def __getitem__(*args): return _pyxdkbibtex.mappairstringstringstring___getitem__(*args)
    def __setitem__(*args): return _pyxdkbibtex.mappairstringstringstring___setitem__(*args)
    def __delitem__(*args): return _pyxdkbibtex.mappairstringstringstring___delitem__(*args)
    def has_key(*args): return _pyxdkbibtex.mappairstringstringstring_has_key(*args)
    def keys(*args): return _pyxdkbibtex.mappairstringstringstring_keys(*args)
    def values(*args): return _pyxdkbibtex.mappairstringstringstring_values(*args)
    def items(*args): return _pyxdkbibtex.mappairstringstringstring_items(*args)
    def __contains__(*args): return _pyxdkbibtex.mappairstringstringstring___contains__(*args)
    def __iter__(*args): return _pyxdkbibtex.mappairstringstringstring___iter__(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_mappairstringstringstring):
        try:
            if self.thisown: destroy(self)
        except: pass

class mappairstringstringstringPtr(mappairstringstringstring):
    def __init__(self, this):
        _swig_setattr(self, mappairstringstringstring, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, mappairstringstringstring, 'thisown', 0)
        _swig_setattr(self, mappairstringstringstring,self.__class__,mappairstringstringstring)
_pyxdkbibtex.mappairstringstringstring_swigregister(mappairstringstringstringPtr)

Braced = _pyxdkbibtex.Braced
Quoted = _pyxdkbibtex.Quoted
Number = _pyxdkbibtex.Number
String = _pyxdkbibtex.String
class ValuePart(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ValuePart, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ValuePart, name)
    def __repr__(self):
        return "<C xdkbib::ValuePart instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, ValuePart, 'this', _pyxdkbibtex.new_ValuePart(*args))
        _swig_setattr(self, ValuePart, 'thisown', 1)
    def type(*args): return _pyxdkbibtex.ValuePart_type(*args)
    def content(*args): return _pyxdkbibtex.ValuePart_content(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_ValuePart):
        try:
            if self.thisown: destroy(self)
        except: pass

class ValuePartPtr(ValuePart):
    def __init__(self, this):
        _swig_setattr(self, ValuePart, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ValuePart, 'thisown', 0)
        _swig_setattr(self, ValuePart,self.__class__,ValuePart)
_pyxdkbibtex.ValuePart_swigregister(ValuePartPtr)

formatBibTeX = _pyxdkbibtex.formatBibTeX

class Field(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Field, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Field, name)
    def __repr__(self):
        return "<C xdkbib::Field instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Field, 'this', _pyxdkbibtex.new_Field(*args))
        _swig_setattr(self, Field, 'thisown', 1)
    def name(*args): return _pyxdkbibtex.Field_name(*args)
    def valueParts(*args): return _pyxdkbibtex.Field_valueParts(*args)
    def line(*args): return _pyxdkbibtex.Field_line(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_Field):
        try:
            if self.thisown: destroy(self)
        except: pass

class FieldPtr(Field):
    def __init__(self, this):
        _swig_setattr(self, Field, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Field, 'thisown', 0)
        _swig_setattr(self, Field,self.__class__,Field)
_pyxdkbibtex.Field_swigregister(FieldPtr)

class FieldHandle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FieldHandle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FieldHandle, name)
    def __repr__(self):
        return "<C xdkbib::FieldHandle instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, FieldHandle, 'this', _pyxdkbibtex.new_FieldHandle(*args))
        _swig_setattr(self, FieldHandle, 'thisown', 1)
    def __deref__(*args): return _pyxdkbibtex.FieldHandle___deref__(*args)
    def name(*args): return _pyxdkbibtex.FieldHandle_name(*args)
    def value(*args): return _pyxdkbibtex.FieldHandle_value(*args)
    def isMissing(*args): return _pyxdkbibtex.FieldHandle_isMissing(*args)
    def add(*args): return _pyxdkbibtex.FieldHandle_add(*args)
    def __lshift__(*args): return _pyxdkbibtex.FieldHandle___lshift__(*args)
    def __iadd__(*args): return _pyxdkbibtex.FieldHandle___iadd__(*args)
    def clear(*args): return _pyxdkbibtex.FieldHandle_clear(*args)
    def entry(*args): return _pyxdkbibtex.FieldHandle_entry(*args)
    def next(*args): return _pyxdkbibtex.FieldHandle_next(*args)
    def __str__(*args): return _pyxdkbibtex.FieldHandle___str__(*args)
    def __nonzero__(*args): return _pyxdkbibtex.FieldHandle___nonzero__(*args)
    def valueParts(*args): return _pyxdkbibtex.FieldHandle_valueParts(*args)
    def line(*args): return _pyxdkbibtex.FieldHandle_line(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_FieldHandle):
        try:
            if self.thisown: destroy(self)
        except: pass

class FieldHandlePtr(FieldHandle):
    def __init__(self, this):
        _swig_setattr(self, FieldHandle, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, FieldHandle, 'thisown', 0)
        _swig_setattr(self, FieldHandle,self.__class__,FieldHandle)
_pyxdkbibtex.FieldHandle_swigregister(FieldHandlePtr)

class Entry(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Entry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Entry, name)
    def __repr__(self):
        return "<C xdkbib::Entry instance at %s>" % (self.this,)
    def __del__(self, destroy=_pyxdkbibtex.delete_Entry):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __init__(self, *args):
        _swig_setattr(self, Entry, 'this', _pyxdkbibtex.new_Entry(*args))
        _swig_setattr(self, Entry, 'thisown', 1)
    def type(*args): return _pyxdkbibtex.Entry_type(*args)
    def key(*args): return _pyxdkbibtex.Entry_key(*args)
    def line(*args): return _pyxdkbibtex.Entry_line(*args)
    def comment(*args): return _pyxdkbibtex.Entry_comment(*args)
    def setComment(*args): return _pyxdkbibtex.Entry_setComment(*args)
    def addField(*args): return _pyxdkbibtex.Entry_addField(*args)
    def hasField(*args): return _pyxdkbibtex.Entry_hasField(*args)
    def field(*args): return _pyxdkbibtex.Entry_field(*args)
    def firstField(*args): return _pyxdkbibtex.Entry_firstField(*args)
    def sortKey(*args): return _pyxdkbibtex.Entry_sortKey(*args)
    def setSortKey(*args): return _pyxdkbibtex.Entry_setSortKey(*args)
    def fields(*args): return _pyxdkbibtex.Entry_fields(*args)
    def longestFieldName(*args): return _pyxdkbibtex.Entry_longestFieldName(*args)

class EntryPtr(Entry):
    def __init__(self, this):
        _swig_setattr(self, Entry, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Entry, 'thisown', 0)
        _swig_setattr(self, Entry,self.__class__,Entry)
_pyxdkbibtex.Entry_swigregister(EntryPtr)

class FileEntry(Entry):
    __swig_setmethods__ = {}
    for _s in [Entry]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileEntry, name, value)
    __swig_getmethods__ = {}
    for _s in [Entry]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, FileEntry, name)
    def __repr__(self):
        return "<C xdkbib::FileEntry instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, FileEntry, 'this', _pyxdkbibtex.new_FileEntry(*args))
        _swig_setattr(self, FileEntry, 'thisown', 1)
    def __del__(self, destroy=_pyxdkbibtex.delete_FileEntry):
        try:
            if self.thisown: destroy(self)
        except: pass

class FileEntryPtr(FileEntry):
    def __init__(self, this):
        _swig_setattr(self, FileEntry, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, FileEntry, 'thisown', 0)
        _swig_setattr(self, FileEntry,self.__class__,FileEntry)
_pyxdkbibtex.FileEntry_swigregister(FileEntryPtr)

class File(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, File, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, File, name)
    def __repr__(self):
        return "<C xdkbib::File instance at %s>" % (self.this,)
    StrictQuote = _pyxdkbibtex.File_StrictQuote
    WarnQuote = _pyxdkbibtex.File_WarnQuote
    AcceptQuote = _pyxdkbibtex.File_AcceptQuote
    def __init__(self, *args):
        _swig_setattr(self, File, 'this', _pyxdkbibtex.new_File(*args))
        _swig_setattr(self, File, 'thisown', 1)
    def __del__(self, destroy=_pyxdkbibtex.delete_File):
        try:
            if self.thisown: destroy(self)
        except: pass
    def readFromFile(*args): return _pyxdkbibtex.File_readFromFile(*args)
    def preambleComponents(*args): return _pyxdkbibtex.File_preambleComponents(*args)
    def entries(*args): return _pyxdkbibtex.File_entries(*args)
    def strings(*args): return _pyxdkbibtex.File_strings(*args)
    def preamble(*args): return _pyxdkbibtex.File_preamble(*args)
    def stringText(*args): return _pyxdkbibtex.File_stringText(*args)
    def comment(*args): return _pyxdkbibtex.File_comment(*args)
    def setComment(*args): return _pyxdkbibtex.File_setComment(*args)
    def clearPreamble(*args): return _pyxdkbibtex.File_clearPreamble(*args)
    def addToPreamble(*args): return _pyxdkbibtex.File_addToPreamble(*args)
    def addEntry(*args): return _pyxdkbibtex.File_addEntry(*args)
    def clearEntries(*args): return _pyxdkbibtex.File_clearEntries(*args)
    def addToString(*args): return _pyxdkbibtex.File_addToString(*args)
    def clearStrings(*args): return _pyxdkbibtex.File_clearStrings(*args)

class FilePtr(File):
    def __init__(self, this):
        _swig_setattr(self, File, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, File, 'thisown', 0)
        _swig_setattr(self, File,self.__class__,File)
_pyxdkbibtex.File_swigregister(FilePtr)

Raw = _pyxdkbibtex.Raw
BracesStripped = _pyxdkbibtex.BracesStripped
CommandStripped = _pyxdkbibtex.CommandStripped
class Text(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Text, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Text, name)
    def __repr__(self):
        return "<C xdkbib::Text instance at %s>" % (self.this,)
    def clone(*args): return _pyxdkbibtex.Text_clone(*args)
    def __init__(self, *args):
        _swig_setattr(self, Text, 'this', _pyxdkbibtex.new_Text(*args))
        _swig_setattr(self, Text, 'thisown', 1)
    def __del__(self, destroy=_pyxdkbibtex.delete_Text):
        try:
            if self.thisown: destroy(self)
        except: pass
    def readFrom(*args): return _pyxdkbibtex.Text_readFrom(*args)
    def content(*args): return _pyxdkbibtex.Text_content(*args)
    def hasContent(*args): return _pyxdkbibtex.Text_hasContent(*args)
    def nbWords(*args): return _pyxdkbibtex.Text_nbWords(*args)
    def words(*args): return _pyxdkbibtex.Text_words(*args)
    def add(*args): return _pyxdkbibtex.Text_add(*args)
    def clear(*args): return _pyxdkbibtex.Text_clear(*args)
    def translate(*args): return _pyxdkbibtex.Text_translate(*args)

class TextPtr(Text):
    def __init__(self, this):
        _swig_setattr(self, Text, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Text, 'thisown', 0)
        _swig_setattr(self, Text,self.__class__,Text)
_pyxdkbibtex.Text_swigregister(TextPtr)

class Word(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Word, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Word, name)
    def __repr__(self):
        return "<C xdkbib::Word instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Word, 'this', _pyxdkbibtex.new_Word(*args))
        _swig_setattr(self, Word, 'thisown', 1)
    def __del__(self, destroy=_pyxdkbibtex.delete_Word):
        try:
            if self.thisown: destroy(self)
        except: pass
    def clone(*args): return _pyxdkbibtex.Word_clone(*args)
    def content(*args): return _pyxdkbibtex.Word_content(*args)
    def hasContent(*args): return _pyxdkbibtex.Word_hasContent(*args)
    def nbLetters(*args): return _pyxdkbibtex.Word_nbLetters(*args)
    def letters(*args): return _pyxdkbibtex.Word_letters(*args)
    def add(*args): return _pyxdkbibtex.Word_add(*args)
    def clear(*args): return _pyxdkbibtex.Word_clear(*args)
    def hasPseudoLetters(*args): return _pyxdkbibtex.Word_hasPseudoLetters(*args)

class WordPtr(Word):
    def __init__(self, this):
        _swig_setattr(self, Word, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Word, 'thisown', 0)
        _swig_setattr(self, Word,self.__class__,Word)
_pyxdkbibtex.Word_swigregister(WordPtr)

class Letter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Letter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Letter, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<C xdkbib::Letter instance at %s>" % (self.this,)
    def __del__(self, destroy=_pyxdkbibtex.delete_Letter):
        try:
            if self.thisown: destroy(self)
        except: pass
    def clone(*args): return _pyxdkbibtex.Letter_clone(*args)
    def content(*args): return _pyxdkbibtex.Letter_content(*args)
    def hasContent(*args): return _pyxdkbibtex.Letter_hasContent(*args)
    def isSingle(*args): return _pyxdkbibtex.Letter_isSingle(*args)
    def isPseudo(*args): return _pyxdkbibtex.Letter_isPseudo(*args)
    def isToken(*args): return _pyxdkbibtex.Letter_isToken(*args)
    def asSingle(*args): return _pyxdkbibtex.Letter_asSingle(*args)
    def asPseudo(*args): return _pyxdkbibtex.Letter_asPseudo(*args)
    def asToken(*args): return _pyxdkbibtex.Letter_asToken(*args)
    def isTheSingle(*args): return _pyxdkbibtex.Letter_isTheSingle(*args)
    def isTheToken(*args): return _pyxdkbibtex.Letter_isTheToken(*args)

class LetterPtr(Letter):
    def __init__(self, this):
        _swig_setattr(self, Letter, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Letter, 'thisown', 0)
        _swig_setattr(self, Letter,self.__class__,Letter)
_pyxdkbibtex.Letter_swigregister(LetterPtr)

class SingleLetter(Letter):
    __swig_setmethods__ = {}
    for _s in [Letter]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, SingleLetter, name, value)
    __swig_getmethods__ = {}
    for _s in [Letter]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, SingleLetter, name)
    def __repr__(self):
        return "<C xdkbib::SingleLetter instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, SingleLetter, 'this', _pyxdkbibtex.new_SingleLetter(*args))
        _swig_setattr(self, SingleLetter, 'thisown', 1)
    def clone(*args): return _pyxdkbibtex.SingleLetter_clone(*args)
    def character(*args): return _pyxdkbibtex.SingleLetter_character(*args)
    def content(*args): return _pyxdkbibtex.SingleLetter_content(*args)
    def isSingle(*args): return _pyxdkbibtex.SingleLetter_isSingle(*args)
    def asSingle(*args): return _pyxdkbibtex.SingleLetter_asSingle(*args)
    def isTheSingle(*args): return _pyxdkbibtex.SingleLetter_isTheSingle(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_SingleLetter):
        try:
            if self.thisown: destroy(self)
        except: pass

class SingleLetterPtr(SingleLetter):
    def __init__(self, this):
        _swig_setattr(self, SingleLetter, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, SingleLetter, 'thisown', 0)
        _swig_setattr(self, SingleLetter,self.__class__,SingleLetter)
_pyxdkbibtex.SingleLetter_swigregister(SingleLetterPtr)

class PseudoLetter(Letter):
    __swig_setmethods__ = {}
    for _s in [Letter]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, PseudoLetter, name, value)
    __swig_getmethods__ = {}
    for _s in [Letter]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, PseudoLetter, name)
    def __repr__(self):
        return "<C xdkbib::PseudoLetter instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, PseudoLetter, 'this', _pyxdkbibtex.new_PseudoLetter(*args))
        _swig_setattr(self, PseudoLetter, 'thisown', 1)
    def clone(*args): return _pyxdkbibtex.PseudoLetter_clone(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_PseudoLetter):
        try:
            if self.thisown: destroy(self)
        except: pass
    def text(*args): return _pyxdkbibtex.PseudoLetter_text(*args)
    def content(*args): return _pyxdkbibtex.PseudoLetter_content(*args)
    def isPseudo(*args): return _pyxdkbibtex.PseudoLetter_isPseudo(*args)
    def asPseudo(*args): return _pyxdkbibtex.PseudoLetter_asPseudo(*args)

class PseudoLetterPtr(PseudoLetter):
    def __init__(self, this):
        _swig_setattr(self, PseudoLetter, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, PseudoLetter, 'thisown', 0)
        _swig_setattr(self, PseudoLetter,self.__class__,PseudoLetter)
_pyxdkbibtex.PseudoLetter_swigregister(PseudoLetterPtr)

class TokenLetter(Letter):
    __swig_setmethods__ = {}
    for _s in [Letter]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TokenLetter, name, value)
    __swig_getmethods__ = {}
    for _s in [Letter]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TokenLetter, name)
    def __repr__(self):
        return "<C xdkbib::TokenLetter instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TokenLetter, 'this', _pyxdkbibtex.new_TokenLetter(*args))
        _swig_setattr(self, TokenLetter, 'thisown', 1)
    def clone(*args): return _pyxdkbibtex.TokenLetter_clone(*args)
    def token(*args): return _pyxdkbibtex.TokenLetter_token(*args)
    def content(*args): return _pyxdkbibtex.TokenLetter_content(*args)
    def isToken(*args): return _pyxdkbibtex.TokenLetter_isToken(*args)
    def asToken(*args): return _pyxdkbibtex.TokenLetter_asToken(*args)
    def isTheToken(*args): return _pyxdkbibtex.TokenLetter_isTheToken(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_TokenLetter):
        try:
            if self.thisown: destroy(self)
        except: pass

class TokenLetterPtr(TokenLetter):
    def __init__(self, this):
        _swig_setattr(self, TokenLetter, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TokenLetter, 'thisown', 0)
        _swig_setattr(self, TokenLetter,self.__class__,TokenLetter)
_pyxdkbibtex.TokenLetter_swigregister(TokenLetterPtr)

class Dictionary(mappairstringstringstring):
    __swig_setmethods__ = {}
    for _s in [mappairstringstringstring]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, Dictionary, name, value)
    __swig_getmethods__ = {}
    for _s in [mappairstringstringstring]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, Dictionary, name)
    def __repr__(self):
        return "<C xdkbib::Dictionary instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Dictionary, 'this', _pyxdkbibtex.new_Dictionary(*args))
        _swig_setattr(self, Dictionary, 'thisown', 1)
    def __del__(self, destroy=_pyxdkbibtex.delete_Dictionary):
        try:
            if self.thisown: destroy(self)
        except: pass

class DictionaryPtr(Dictionary):
    def __init__(self, this):
        _swig_setattr(self, Dictionary, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Dictionary, 'thisown', 0)
        _swig_setattr(self, Dictionary,self.__class__,Dictionary)
_pyxdkbibtex.Dictionary_swigregister(DictionaryPtr)


isoaccents = _pyxdkbibtex.isoaccents
class Author(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Author, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Author, name)
    def __repr__(self):
        return "<C xdkbib::Author instance at %s>" % (self.this,)
    def __init__(self, *args):
        _swig_setattr(self, Author, 'this', _pyxdkbibtex.new_Author(*args))
        _swig_setattr(self, Author, 'thisown', 1)
    def first(*args): return _pyxdkbibtex.Author_first(*args)
    def von(*args): return _pyxdkbibtex.Author_von(*args)
    def jr(*args): return _pyxdkbibtex.Author_jr(*args)
    def last(*args): return _pyxdkbibtex.Author_last(*args)
    def firstJoin(*args): return _pyxdkbibtex.Author_firstJoin(*args)
    def vonJoin(*args): return _pyxdkbibtex.Author_vonJoin(*args)
    def jrJoin(*args): return _pyxdkbibtex.Author_jrJoin(*args)
    def lastJoin(*args): return _pyxdkbibtex.Author_lastJoin(*args)
    def pushFirst(*args): return _pyxdkbibtex.Author_pushFirst(*args)
    def pushVon(*args): return _pyxdkbibtex.Author_pushVon(*args)
    def pushJr(*args): return _pyxdkbibtex.Author_pushJr(*args)
    def pushLast(*args): return _pyxdkbibtex.Author_pushLast(*args)
    def __del__(self, destroy=_pyxdkbibtex.delete_Author):
        try:
            if self.thisown: destroy(self)
        except: pass

class AuthorPtr(Author):
    def __init__(self, this):
        _swig_setattr(self, Author, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Author, 'thisown', 0)
        _swig_setattr(self, Author,self.__class__,Author)
_pyxdkbibtex.Author_swigregister(AuthorPtr)

class AuthorList(vectorauthor):
    __swig_setmethods__ = {}
    for _s in [vectorauthor]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, AuthorList, name, value)
    __swig_getmethods__ = {}
    for _s in [vectorauthor]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, AuthorList, name)
    def __repr__(self):
        return "<C xdkbib::AuthorList instance at %s>" % (self.this,)
    def readFrom(*args): return _pyxdkbibtex.AuthorList_readFrom(*args)
    def __init__(self, *args):
        _swig_setattr(self, AuthorList, 'this', _pyxdkbibtex.new_AuthorList(*args))
        _swig_setattr(self, AuthorList, 'thisown', 1)
    def __del__(self, destroy=_pyxdkbibtex.delete_AuthorList):
        try:
            if self.thisown: destroy(self)
        except: pass

class AuthorListPtr(AuthorList):
    def __init__(self, this):
        _swig_setattr(self, AuthorList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, AuthorList, 'thisown', 0)
        _swig_setattr(self, AuthorList,self.__class__,AuthorList)
_pyxdkbibtex.AuthorList_swigregister(AuthorListPtr)


