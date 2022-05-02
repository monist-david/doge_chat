from flask import Flask, render_template, request

# from deploy_doge_2.deploy_doge import find_response_rule, find_multiple_response_acquired, find_response_open, \
#     compare_score, compare_score_second, tags_rule, intents_result, data_acquire, model_rank_updown, \
#     tokenizer_rank_updown

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")  # to send context to html


@app.route("/get")
def get_bot_response():
    # context = []
    # utterance = ''
    # bot_name = "Doge"
    # print("Let's chat! (type 'quit' to exit)")
    # userText = request.args.get("msg")
    # sentence = input("You: ")
    # if utterance == '' and sentence != '':
    #     utterance = sentence + '</s>'
    # else:
    #     utterance += '<s>' + sentence + '</s>'
    # context.append(sentence)
    # context_rank = context
    # if len(context) >= 10:
    #     context = context[1:]
    # if len(context_rank) >= 3:
    #     context_rank = context_rank[-3:]
    # ## rule model
    # result_rule = find_response_rule(sentence, tags_rule, intents_result)
    # if result_rule != "Unknown":
    #     print('\n')
    #     # print("RULE MODEL")
    #     print(f"{bot_name}: {result_rule}")
    #     context.append(result_rule)
    #     # utterance += '<s>' + str(result_rule) + '</s>'
    # else:
    #     result_acquire = find_multiple_response_acquired(context, data_acquire)
    #     result_final = find_response_open(context, result_acquire)
    #     result_acquire.append(result_final)
    #     print(result_acquire)
    #     # result_test = rank_response(context, result_acquire)
    #     result_final_updown = compare_score(context, result_acquire, model_rank_updown, tokenizer_rank_updown)[0]
    #     if result_final_updown in context:
    #         result_final_updown = compare_score_second(context, result_acquire, model_rank_updown,
    #                                                    tokenizer_rank_updown)
    #     context.append(result_final_updown)
    #     print("FINAL MODEL")
    #     print(f"{bot_name}: {result_final_updown}")
    #     print("HISTORY", context)
    #     print("\n")
    # return result_final_updown
    userText = request.args.get("msg")
    return userText


if __name__ == "__main__":
    app.run(debug=True)
