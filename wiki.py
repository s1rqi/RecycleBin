import wikipedia
wikipedia.set_lang("ja")

while True:
    i = input("\nSearch> ")
    try:
        result = wikipedia.page(i)
        print(result.summary)

    except wikipedia.DisambiguationError as e:
        print("もしかして:\n"+"\n".join(e.options))

    except wikipedia.exceptions.PageError:
        print("何言ってるかわかんねーー！！")

    except wikipedia.exceptions.WikipediaException:
        print("空白やめろー！！")

    except:
        print("エラー！！！！！！！！！！！")
