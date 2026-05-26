from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import Flowable
from reportlab.platypus import HRFlowable
from reportlab.platypus import PageBreak
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.platypus import TableStyle


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "output" / "pdf" / "ether_business_plan_2026-05-18.pdf"

PRIMARY = colors.HexColor("#26334D")
PRIMARY_DARK = colors.HexColor("#141B2D")
ACCENT = colors.HexColor("#A1783A")
ACCENT_SOFT = colors.HexColor("#F6F0E6")
LINE = colors.HexColor("#D8DEE8")
TEXT = colors.HexColor("#202733")
MUTED = colors.HexColor("#667085")
SOFT = colors.HexColor("#F8F9FB")
WARN = colors.HexColor("#8A5A00")


def register_fonts() -> tuple[str, str]:
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))
    return "HeiseiKakuGo-W5", "HeiseiMin-W3"


FONT_HEADING, FONT_BODY = register_fonts()


def style(name: str, size: int, leading: int, **kwargs) -> ParagraphStyle:
    return ParagraphStyle(
        name,
        fontName=kwargs.pop("fontName", FONT_BODY),
        fontSize=size,
        leading=leading,
        textColor=kwargs.pop("textColor", TEXT),
        alignment=kwargs.pop("alignment", TA_LEFT),
        wordWrap="CJK",
        spaceAfter=kwargs.pop("spaceAfter", 0),
        spaceBefore=kwargs.pop("spaceBefore", 0),
        **kwargs,
    )


STYLES = {
    "title": style("title", 25, 34, fontName=FONT_HEADING, textColor=PRIMARY_DARK, alignment=TA_LEFT),
    "subtitle": style("subtitle", 10.8, 16, fontName=FONT_HEADING, textColor=MUTED, alignment=TA_LEFT),
    "cover_title": style("cover_title", 25, 33, fontName=FONT_HEADING, textColor=PRIMARY_DARK, alignment=TA_LEFT),
    "cover_subtitle": style("cover_subtitle", 10.8, 16, fontName=FONT_HEADING, textColor=MUTED, alignment=TA_LEFT),
    "h1": style("h1", 15.5, 21, fontName=FONT_HEADING, textColor=PRIMARY_DARK, spaceAfter=7),
    "h2": style("h2", 11.5, 16, fontName=FONT_HEADING, textColor=PRIMARY_DARK, spaceAfter=5),
    "body": style("body", 9.3, 14.6),
    "small": style("small", 8, 11.5, textColor=MUTED),
    "table": style("table", 8.4, 12.8),
    "table_head": style("table_head", 8.6, 12.6, fontName=FONT_HEADING, textColor=colors.white),
    "note": style("note", 8.3, 12.2, fontName=FONT_HEADING, textColor=WARN),
    "center": style("center", 9, 13.5, alignment=TA_CENTER),
}


class Badge(Flowable):
    def __init__(self, text: str, width: float = 42 * mm):
        super().__init__()
        self.text = text
        self.width = width
        self.height = 11 * mm

    def draw(self) -> None:
        self.canv.setFillColor(ACCENT_SOFT)
        self.canv.setStrokeColor(colors.HexColor("#E2D3B8"))
        self.canv.roundRect(0, 0, self.width, self.height, 2, fill=1, stroke=1)
        self.canv.setFillColor(colors.HexColor("#6E4D17"))
        self.canv.setFont(FONT_HEADING, 8.3)
        self.canv.drawCentredString(self.width / 2, 3.6 * mm, self.text)


def p(text: str, key: str = "body") -> Paragraph:
    return Paragraph(text, STYLES[key])


def section(title: str) -> list:
    return [
        Spacer(1, 2.5 * mm),
        p(title, "h1"),
        HRFlowable(width="100%", thickness=0.65, color=LINE, spaceAfter=3.5 * mm),
    ]


def bullet(text: str) -> Paragraph:
    return Paragraph(f"<font color='#26334D'>●</font> {text}", STYLES["body"])


def make_table(data: list[list], widths: list[float], header: bool = False) -> Table:
    table = Table(data, colWidths=widths, hAlign="LEFT", repeatRows=1 if header else 0)
    commands = [
        ("FONTNAME", (0, 0), (-1, -1), FONT_BODY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.45, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
    ]
    if header:
        commands.extend(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ]
        )
    else:
        commands.append(("BACKGROUND", (0, 0), (0, -1), SOFT))
    table.setStyle(TableStyle(commands))
    return table


def cover_banner(width: float) -> Table:
    table = Table(
        [
            [p("事業計画書", "cover_title")],
            [p("会社紹介資料・取扱サービス一覧を含む", "cover_subtitle")],
        ],
        colWidths=[width],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), SOFT),
                ("BOX", (0, 0), (-1, -1), 0.6, LINE),
                ("LINEBEFORE", (0, 0), (0, -1), 4, ACCENT),
                ("LEFTPADDING", (0, 0), (-1, -1), 18),
                ("RIGHTPADDING", (0, 0), (-1, -1), 16),
                ("TOPPADDING", (0, 0), (-1, 0), 18),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 1),
                ("TOPPADDING", (0, 1), (-1, 1), 0),
                ("BOTTOMPADDING", (0, 1), (-1, 1), 15),
            ]
        )
    )
    return table


def header_footer(canvas, doc) -> None:
    canvas.saveState()
    width, height = A4
    canvas.setFillColor(PRIMARY)
    canvas.rect(0, height - 4 * mm, width, 4 * mm, fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(doc.leftMargin, height - 17 * mm, width - doc.rightMargin, height - 17 * mm)
    canvas.setFillColor(PRIMARY_DARK)
    canvas.setFont(FONT_HEADING, 7.8)
    canvas.drawString(doc.leftMargin, height - 12 * mm, "Ether合同会社 事業計画書")
    canvas.setFillColor(MUTED)
    canvas.setFont(FONT_BODY, 7.6)
    canvas.drawRightString(width - doc.rightMargin, height - 12 * mm, "提出日 2026年5月18日")
    canvas.setFillColor(MUTED)
    canvas.setFont(FONT_BODY, 7.1)
    canvas.drawString(doc.leftMargin, 11 * mm, "Ether合同会社 (Ether LLC) - 〒160-0022 東京都新宿区新宿四丁目3番15号")
    canvas.drawRightString(width - doc.rightMargin, 11 * mm, f"{doc.page}")
    canvas.restoreState()


def build_story() -> list:
    w = A4[0] - 34 * mm - 34 * mm
    story = []

    story.extend(
        [
            Spacer(1, 10 * mm),
            cover_banner(w),
            Spacer(1, 7 * mm),
            Badge("事業内容確認用"),
            Spacer(1, 8 * mm),
            p(
                "本資料は、設立間もないため契約書・請求書・納品書等を現時点で提出できない場合の、"
                "事業内容確認資料として作成したものです。登記上の商号・本店所在地を明記し、"
                "今後運営予定の事業、提供予定サービス、収益化方針、管理体制を整理しています。",
                "body",
            ),
            Spacer(1, 7 * mm),
            make_table(
                [
                    [p("商号", "table"), p("Ether合同会社 (Ether LLC)", "table")],
                    [p("代表社員", "table"), p("増田 創 (Soh Masuda)", "table")],
                    [p("登記上の本店所在地", "table"), p("〒160-0022 東京都新宿区新宿四丁目3番15号", "table")],
                    [p("法人番号", "table"), p("4011103016903", "table")],
                    [p("設立年月日", "table"), p("2025年12月22日", "table")],
                    [p("資本金", "table"), p("1円", "table")],
                    [p("連絡先", "table"), p("so.masuda.2003@ether-llc.com", "table")],
                    [p("公開サイト", "table"), p("https://ether-llc.com", "table")],
                ],
                [38 * mm, w - 38 * mm],
            ),
            PageBreak(),
        ]
    )

    story.extend(section("1. 事業概要"))
    story.extend(
        [
            p(
                "Ether合同会社は、東京を拠点に、ソフトウェア開発、Ethereumの自社保有、"
                "関連する文化事業を行う会社です。現在は、iOSアプリ開発を中心に自社プロダクトの準備を進め、"
                "同時にSwiftUI、iOSアプリ、Web3関連の開発相談を受け付ける体制を整えています。",
            ),
            Spacer(1, 4 * mm),
            make_table(
                [
                    [p("領域", "table_head"), p("事業内容・現状", "table_head")],
                    [
                        p("自社ソフトウェア", "table"),
                        p(
                            "日々の感謝を記録するiOSアプリ GratefulMoments の設計・開発・運用。"
                            "現在は開発中で、App Store公開準備中。",
                            "table",
                        ),
                    ],
                    [
                        p("開発相談・実装支援", "table"),
                        p(
                            "SwiftUI、iOSアプリ、Web3関連の設計相談、試作、実装支援。"
                            "問い合わせ受付体制を整備中。",
                            "table",
                        ),
                    ],
                    [
                        p("Ethereum保有", "table"),
                        p(
                            "会社資産としてEthereum (ETH) を長期保有する方針。"
                            "自己資金で取得・保有し、顧客資産の預託、投資勧誘、暗号資産交換業は行わない。",
                            "table",
                        ),
                    ],
                    [
                        p("文化事業", "table"),
                        p("ソフトウェア、Ethereum、創作に関する公開可能な活動を順次整理。初期検討段階。", "table"),
                    ],
                ],
                [38 * mm, w - 38 * mm],
                header=True,
            ),
            Spacer(1, 5 * mm),
            bullet("主たる事業は、現時点では自社ソフトウェア開発と開発相談・実装支援です。"),
            bullet("Ethereum保有は会社資産の管理方針であり、第三者資産の預託や金融商品の販売を目的としません。"),
            bullet("受注・売上の発生前であるため、契約書や請求書ではなく、本資料により事業計画を説明します。"),
            PageBreak(),
        ]
    )

    story.extend(section("2. 取扱サービス・商品カタログ"))
    story.extend(
        [
            p(
                "提出要件で例示されている「事業案内」および「取扱商品カタログ」に相当する情報として、"
                "提供予定のサービス・プロダクトを以下に整理します。価格・提供範囲は正式な申込受付時に個別見積または利用規約で確定します。",
            ),
            Spacer(1, 4 * mm),
            make_table(
                [
                    [p("名称", "table_head"), p("対象顧客・提供内容・収益化方針", "table_head")],
                    [
                        p("GratefulMoments", "table"),
                        p(
                            "対象顧客: 個人利用者。<br/>"
                            "提供内容: タイトル、メモ、写真で日々の感謝を記録するiOSアプリ。<br/>"
                            "収益化方針: 無料提供を起点に、追加機能・買い切り・サブスクリプション等を検討。",
                            "table",
                        ),
                    ],
                    [
                        p("iOSアプリ開発相談", "table"),
                        p(
                            "対象顧客: 個人事業主・法人。<br/>"
                            "提供内容: SwiftUI、画面設計、プロトタイプ、実装レビュー、運用相談。<br/>"
                            "収益化方針: 個別見積。小規模相談から受託開発まで段階的に対応。",
                            "table",
                        ),
                    ],
                    [
                        p("Web3関連開発相談", "table"),
                        p(
                            "対象顧客: 法人・研究者・個人開発者。<br/>"
                            "提供内容: Ethereum関連の技術調査、ウォレット周辺の設計相談、実装検証。<br/>"
                            "収益化方針: 個別見積。金融商品販売や暗号資産交換業に該当する業務は行わない。",
                            "table",
                        ),
                    ],
                    [
                        p("技術コンテンツ・文化活動", "table"),
                        p(
                            "対象顧客: 一般閲覧者・協業先。<br/>"
                            "提供内容: 開発記録、技術記事、文化的プロジェクトの公開。<br/>"
                            "収益化方針: 当面は広報・信用形成を目的とし、収益化は慎重に検討。",
                            "table",
                        ),
                    ],
                ],
                [45 * mm, w - 45 * mm],
                header=True,
            ),
            Spacer(1, 6 * mm),
            p("公開・確認可能な情報", "h2"),
            bullet("会社サイト: https://ether-llc.com"),
            bullet("ソフトウェア開発ページ: https://ether-llc.com/software/"),
            bullet("GitHubリポジトリ: https://github.com/masuda-so/GratefulMoments"),
            bullet("問い合わせ窓口: so.masuda.2003@ether-llc.com"),
            PageBreak(),
        ]
    )

    story.extend(section("3. 収益化計画・営業活動"))
    story.extend(
        [
            p(
                "設立初期のため、本資料作成日時点では、請求書、納品書、受注書、売上管理画面の提出対象となる"
                "確定取引はありません。今後は、問い合わせ受付、見積、契約、納品、請求、入金確認の流れを整備し、"
                "会計記録と証憑を保存します。",
            ),
            Spacer(1, 4 * mm),
            make_table(
                [
                    [p("時期", "table_head"), p("活動計画・確認可能になる予定の証憑", "table_head")],
                    [
                        p("2026年5月-6月", "table"),
                        p(
                            "活動計画: GratefulMomentsの公開準備、問い合わせ導線の整備、提供サービス範囲の明文化。<br/>"
                            "証憑予定: Webサイト、GitHub更新履歴、問い合わせメール記録。",
                            "table",
                        ),
                    ],
                    [
                        p("2026年7月-9月", "table"),
                        p(
                            "活動計画: アプリ審査準備、テスト利用、開発相談の受付開始。<br/>"
                            "証憑予定: テスト記録、見積書、契約書、メールのやり取り。",
                            "table",
                        ),
                    ],
                    [
                        p("2026年10月-2027年3月", "table"),
                        p(
                            "活動計画: 自社アプリの運用改善、小規模な開発支援案件の受注、請求・会計運用の定着。<br/>"
                            "証憑予定: 請求書、納品書、入金記録、会計ソフトの売上記録。",
                            "table",
                        ),
                    ],
                    [
                        p("2027年4月以降", "table"),
                        p(
                            "活動計画: プロダクト機能拡張、受託領域の整理、継続的な公開情報の更新。<br/>"
                            "証憑予定: 売上推移、契約書一式、利用状況レポート。",
                            "table",
                        ),
                    ],
                ],
                [40 * mm, w - 40 * mm],
                header=True,
            ),
            Spacer(1, 6 * mm),
            p("予定している受注・請求フロー", "h2"),
            bullet("問い合わせ受領: メールで相談内容、希望納期、連絡先を確認。"),
            bullet("見積・契約: 作業範囲、納期、成果物、報酬、支払条件を文書化。"),
            bullet("納品・検収: GitHub、ドキュメント、アプリ配布等で成果物を確認。"),
            bullet("請求・保存: 請求書、納品書、入金記録、会計記録を保存。"),
            Spacer(1, 4 * mm),
            p(
                "注記: 本ページの時期・活動は計画であり、確定済み取引や売上実績を示すものではありません。",
                "note",
            ),
            PageBreak(),
        ]
    )

    story.extend(section("4. 運営体制・管理方針"))
    story.extend(
        [
            make_table(
                [
                    [p("項目", "table_head"), p("方針", "table_head")],
                    [
                        p("開発体制", "table"),
                        p("代表社員が要件定義、設計、実装、公開準備、運用管理を担当。必要に応じて外部協力先を検討。", "table"),
                    ],
                    [
                        p("情報管理", "table"),
                        p("業務メール、契約書、請求書、納品物、会計記録を案件単位で保存。個人情報は最小限の取得とする。", "table"),
                    ],
                    [
                        p("会計・売上管理", "table"),
                        p("売上発生後は請求書、入金記録、会計ソフト等により証憑を保管し、税務・会計処理に利用。", "table"),
                    ],
                    [
                        p("法令・リスク", "table"),
                        p("Ethereum関連では自己資金による保有に限定し、顧客資産の預託、投資勧誘、交換業に該当する行為は行わない。", "table"),
                    ],
                    [
                        p("公開情報", "table"),
                        p("会社サイトで会社概要、事業内容、ソフトウェア開発、Ethereum保有方針、問い合わせ先を公開。", "table"),
                    ],
                ],
                [37 * mm, w - 37 * mm],
                header=True,
            ),
            Spacer(1, 7 * mm),
            p("提出要件との対応", "h2"),
            make_table(
                [
                    [p("要件例", "table_head"), p("本資料での対応", "table_head")],
                    [
                        p("登記上の社名・所在地が明記されている事業案内", "table"),
                        p("1ページ目に商号、登記上の本店所在地、法人番号を記載。2ページ目以降に事業案内を記載。", "table"),
                    ],
                    [
                        p("取扱商品カタログ", "table"),
                        p("2ページ目に取扱サービス・商品カタログとして提供予定サービスを整理。", "table"),
                    ],
                    [
                        p("受注や仕入に関わるメール・FAX等", "table"),
                        p("設立初期で確定取引前のため現時点では該当なし。今後は問い合わせ、見積、契約、納品、請求の証憑を保存予定。", "table"),
                    ],
                    [
                        p("収益や売上が確認できる管理画面", "table"),
                        p("売上発生前のため現時点では該当なし。収益化後は会計記録・入金記録・サービス管理画面を保存予定。", "table"),
                    ],
                ],
                [62 * mm, w - 62 * mm],
                header=True,
            ),
            Spacer(1, 8 * mm),
            p(
                "以上の内容により、Ether合同会社の主たる事業、設立初期の状況、今後の運営計画を説明します。",
                "body",
            ),
        ]
    )
    return story


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=17 * mm,
        leftMargin=17 * mm,
        topMargin=23 * mm,
        bottomMargin=20 * mm,
        title="Ether合同会社 事業計画書",
        author="Ether合同会社",
        subject="事業内容確認用 事業計画書",
    )
    doc.build(build_story(), onFirstPage=header_footer, onLaterPages=header_footer)
    print(OUTPUT)


if __name__ == "__main__":
    main()
