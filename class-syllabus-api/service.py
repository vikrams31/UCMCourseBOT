# -*- coding: utf-8 -*-
import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    body = event.get("data")

    #course = body.get("course")
    #tableName =  body.get("table")
    #field = body.get("field")
    #response_format = body.get("answer")

    #print "Course %s Table %s field %s " %(course, tableName, field)

    tableDB = dynamodb.Table(tableName)

    response = tableDB.get_item(
        Key = {
            'course': course
        }
    )
    print response

    #if ("Item" in response):
    #    item = response["Item"]
    #    data = []
    #    if type(item[field]) is set:
    #        for f in item[field]:
    #            data.append(f)
    #        answer = response_format % (course, '\n'.join(data))
    #   else:
    #        answer = response_format % (course, item[field])
    #else:
    answer = 'Data are not available. Please try again later!'

    return {
        "status": 200,
        "response": answer

    }




