import boto3
import decimal

def round_float_to_decimal(value):
    with decimal.localcontext(boto3.dynamodb.types.DYNAMODB_CONTEXT) as ctx:
        ctx.traps[decimal.Inexact] = 0
        ctx.traps[decimal.Rounded] = 0
        return ctx.create_decimal_from_float(value)
