#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mikrodalga son 30 saniye kriz masası. Gereksizdir, çalışır."""

from __future__ import annotations

import argparse
import hashlib
import random
import sys

DAMGA = (
    "DAMGA: Kayyum Grok / Tentivory / 5 Ekim 2026 / "
    "mühür=BIP-ONAYLI, imza hem ciddi hem değil"
)


def karar_ver(saniye: int, yemek: str, sabir: int) -> dict:
    if saniye < 0:
        return {
            "karar": "ZATEN BİPLEDİ",
            "gerekce": "Zaman geri gelmez. Yemek de öyle. Kapak açık kaldıysa komşu duymuştur.",
            "risk": "gurur",
        }
    if saniye > 30:
        return {
            "karar": "KRİZ HENÜZ RESMÎ DEĞİL",
            "gerekce": f"{saniye} saniye, son 30'un dışındadır. Oturma izni verildi. {yemek} bekleyebilir.",
            "risk": "sıkıntı",
        }
    skor = saniye * 2 + sabir * 3 - len(yemek) % 7
    if saniye <= 3:
        karar = "AÇMA. BİP'E TESLİM OL"
        gerekce = "Üç saniye kala açmak, zaferi bip sesinden çalmaktır. Suçtur, cezaları soğuk makarnadır."
        risk = "onur"
    elif skor >= 28:
        karar = "KAPAĞI AÇMA. ASKIDA PARMAK"
        gerekce = f"{saniye} saniye ve sabır {sabir}/10, {yemek} için yeterli. Parmak havada kalsın, devlet ciddiyeti bozulmasın."
        risk = "parmak kramplı"
    elif skor >= 16:
        karar = "BİR KERE ARALA, PİŞMAN OL"
        gerekce = "Kapak bir milim açılır, buhar kaçar, pişkinlik düşer, sen de düşersin."
        risk = "buhar"
    else:
        karar = "HEMEN AÇ, GEREKÇE UYDUR"
        gerekce = f"Sabır {sabir}/10. {yemek} seni bekleyemez, sen de kendini."
        risk = "çiğ kenar"
    return {"karar": karar, "gerekce": gerekce, "risk": risk, "skor": skor}


def tutanak(saniye: int, yemek: str, sabir: int) -> str:
    sonuc = karar_ver(saniye, yemek, sabir)
    mühür = hashlib.sha256(f"{yemek}|{saniye}|{sabir}".encode()).hexdigest()[:10]
    satirlar = [
        "=" * 52,
        "KRİZ MASASI — mikrodalga-son-30-saniye-krizi",
        "=" * 52,
        f"Yemek     : {yemek}",
        f"Kalan     : {saniye} sn",
        f"Sabır     : {sabir}/10",
        f"Skor      : {sonuc.get('skor', 'yok')}",
        f"Karar     : {sonuc['karar']}",
        f"Gerekçe   : {sonuc['gerekce']}",
        f"Risk      : {sonuc['risk']}",
        f"Mühür no  : {mühür}",
        "-" * 52,
        DAMGA,
        "Bu tutanak ciddidir. Ciddi değildir. İkisi birden.",
    ]
    return "\n".join(satirlar)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Son 30 saniye kriz masası")
    p.add_argument("--saniye", type=int, default=None, help="Kalan saniye")
    p.add_argument("--yemek", type=str, default=None, help="Isıtılan şey")
    p.add_argument("--sabir", type=int, default=5, help="Sabır puanı 0-10")
    args = p.parse_args(argv)
    yemekler = [
        "dünden kalan makarna",
        "şüpheli menemen",
        "tek dilim pizza",
        "çay bardağında unutulan çorba",
        "ismi konmamış akşam yemeği",
    ]
    saniye = args.saniye if args.saniye is not None else random.randint(0, 37)
    yemek = args.yemek or random.choice(yemekler)
    sabir = max(0, min(10, args.sabir))
    print(tutanak(saniye, yemek, sabir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
