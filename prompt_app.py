import streamlit as st

# 誕生花＆誕生石データ（英語）
birth_data = {
    1: {"flower": "carnation", "gemstone": "garnet", "color": "deep red"},
    2: {"flower": "violet", "gemstone": "amethyst", "color": "purple"},
    3: {"flower": "daffodil", "gemstone": "aquamarine", "color": "pale blue"},
    4: {"flower": "daisy", "gemstone": "diamond", "color": "clear or white"},
    5: {"flower": "lily of the valley", "gemstone": "emerald", "color": "rich green"},
    6: {"flower": "rose", "gemstone": "pearl", "color": "soft pink or white"},
    7: {"flower": "larkspur", "gemstone": "ruby", "color": "vivid red"},
    8: {"flower": "gladiolus", "gemstone": "peridot", "color": "light green"},
    9: {"flower": "aster", "gemstone": "sapphire", "color": "deep blue"},
    10: {"flower": "marigold", "gemstone": "opal", "color": "multicolor or iridescent"},
    11: {"flower": "chrysanthemum", "gemstone": "topaz", "color": "golden yellow"},
    12: {"flower": "narcissus", "gemstone": "turquoise", "color": "turquoise blue"},
}

# カスタムプロンプト（特定月）
custom_prompts = {
    2: "A delicate violet flower with five rounded, slightly heart-shaped petals, made of amethyst-like crystal. The petals are small, purple, and glowing, with a soft golden stamen in the center. The background is softly blurred with warm golden bokeh.",
    5: "A lily of the valley flower, with multiple small bell-shaped blossoms hanging from a single curved stem. Each blossom is made of translucent emerald crystal, glowing softly. The background features gentle warm bokeh lights.",
    7: "A tall larkspur flower, similar to a delphinium, with multiple narrow-petaled blossoms in vivid ruby red crystal. The blossoms climb up a central stem and shimmer like carved gems. Soft golden bokeh lights fill the background.",
    8: "A gladiolus flower with a tall, sword-like green stem and several trumpet-shaped blossoms aligned vertically. Each bloom is crafted from translucent light green peridot crystal, featuring delicate faceting and gentle refractions. A soft golden stamen glows at the center of each flower. The background is softly blurred with warm golden bokeh, adding a dreamy and elegant atmosphere.",
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

    st.subheader(f"【{month}月】{flower.title()} × {gemstone.title()}")
    st.text_area("プロンプト", value=prompt, height=250)