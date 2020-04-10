# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-27 14:58'
from pre_request.exception import ParamsValueError
from .base import BaseFilter


class EqualFilter(BaseFilter):
    """
    判断数值相等过滤器
    """

    eq_code = 578
    neq_code = 579

    def fmt_error_message(self, code):
        """ 格式化错误消息
        """
        if code == 578:
            return "%s字段必须等于%s!" % (self.key, str(self.rule.eq))

        if code == 579:
            return "%s字段不能等于%s!" % (self.key, str(self.rule.neq))

        return "%s字段未通过`EqualFilter`过滤器检查!" % self.key

    def __call__(self, *args, **kwargs):
        super(EqualFilter, self).__call__()

        # None值不做处理
        if self.rule.allow_empty and self.value is None:
            return self.value

        if self.rule.eq is not None and self.value != self.rule.eq:
            raise ParamsValueError(self.eq_code, filter=self)

        if self.rule.neq is not None and self.value == self.rule.neq:
            raise ParamsValueError(self.neq_code, filter=self)

        return self.value
