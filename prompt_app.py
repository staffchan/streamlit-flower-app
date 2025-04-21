import streamlit as st

# 誕生花＆誕生石データ（英語）
birth_data = {
    1: {"flower": "narcissus", "flower_ja": "水仙", "gemstone": "garnet", "gemstone_ja": "ガーネット", "color": "deep red"},
    2: {"flower": "marguerite", "flower_ja": "マーガレット", "gemstone": "amethyst", "gemstone_ja": "アメジスト", "color": "purple"},
    3: {"flower": "tulip", "flower_ja": "チューリップ", "gemstone": "aquamarine", "gemstone_ja": "アクアマリン", "color": "pale blue"},
    4: {"flower": "cherry blossom", "flower_ja": "桜", "gemstone": "diamond", "gemstone_ja": "ダイヤモンド", "color": "clear or white"},
    5: {"flower": "lily of the valley", "flower_ja": "すずらん", "gemstone": "emerald", "gemstone_ja": "エメラルド", "color": "rich green"},
    6: {"flower": "rose", "flower_ja": "バラ", "gemstone": "pearl", "gemstone_ja": "パール", "color": "soft pink or white"},
    7: {"flower": "lily", "flower_ja": "百合", "gemstone": "ruby", "gemstone_ja": "ルビー", "color": "vivid red"},
    8: {"flower": "sunflower", "flower_ja": "ひまわり", "gemstone": "peridot", "gemstone_ja": "ペリドット", "color": "light green"},
    9: {"flower": "dahlia", "flower_ja": "ダリア", "gemstone": "sapphire", "gemstone_ja": "サファイア", "color": "deep blue"},
    10: {"flower": "gerbera", "flower_ja": "ガーベラ", "gemstone": "opal", "gemstone_ja": "オパール", "color": "multicolor or iridescent"},
    11: {"flower": "chrysanthemum", "flower_ja": "菊", "gemstone": "topaz", "gemstone_ja": "トパーズ", "color": "golden yellow"},
    12: {"flower": "poinsettia", "flower_ja": "ポインセチア", "gemstone": "turquoise", "gemstone_ja": "トルコ石", "color": "turquoise blue"},
}
# カスタムプロンプト（特定月）
custom_prompts = {
    5: "A lily of the valley flower, with multiple small bell-shaped blossoms hanging from a single curved stem. Each blossom is made of translucent emerald crystal, glowing softly. The background features gentle warm bokeh lights.",
    11: "A traditional Japanese-style chrysanthemum with thick, curled yellow petals densely packed into a rounded dome shape. The flower appears voluminous and intricate, each petal made of faceted golden topaz crystal. A subtle golden shimmer glows from within, and the background is softly blurred with warm bokeh lights, enhancing its regal and elegant appearance."
}

# Streamlit UI
st.title("誕生花 × 誕生石 プロンプト生成アプリ")
st.caption("誕生月を選ぶと、その月の花と宝石を使ったプロンプトが表示されます")

month = st.selectbox("誕生月を選んでください", list(range(1, 13)), key="month_select")

# 選んだ月に応じて表示
if month in birth_data:
    data = birth_data[month]
    flower = data["flower"]
    gemstone = data["gemstone"]

    # プロンプト生成
    if month in custom_prompts:
        prompt = custom_prompts[month]
    else:
        color = data["color"]
        prompt = (
            f"A full view of a magical {flower} flower with gemstone-like petals made of {gemstone}, "
            f"featuring a translucent, faceted texture that reflects {color} hues. "
            f"The petals shimmer with soft sparkles. A golden stamen sits at the center, "
            f"and the background glows with gentle bokeh orbs. Macro, ultra-detailed, photorealistic."
        )

    st.subheader(f"【{month}月】{data['flower_ja']} ({flower.title()}) × {gemstone.title()}")
    st.text_area("プロンプト", value=prompt, height=250)