import pytest
from unittest.mock import Mock
from src.combat.attack import AttackType, WeaknessSet, Attack
from src.localization.l_string import LString


class TestWeaknessSet:
    @staticmethod
    def test_weakness_set_initialization():
        weaknesses = {
            'PHYSICAL': 1.5,
            'FIRE': 2
        }
        ws = WeaknessSet(weaknesses)

        assert ws[AttackType.PHYSICAL] == 1.5
        assert ws[AttackType.FIRE] == 2.0

    @staticmethod
    def test_weakness_set_invalid_factor_type():
        weaknesses = {
            'PHYSICAL': 'invalid'  # Should raise TypeError
        }
        with pytest.raises(TypeError, match="Weakness factor must be float or int"):
            WeaknessSet(weaknesses)  # type: ignore

    @staticmethod
    def test_weakness_set_default_value():
        ws = WeaknessSet({})
        for attack_type in AttackType:
            assert ws[attack_type] == 1.0

    @staticmethod
    def test_attack_factor():
        weaknesses = {
            'PHYSICAL': 1.5,
            'FIRE': 2.0
        }
        ws = WeaknessSet(weaknesses)

        attack = Attack(dmg=10, types=[AttackType.PHYSICAL, AttackType.FIRE])
        factor = ws.attack_factor(attack)
        assert factor == (1.5 * 2.0)


class TestAttack:
    # Test for Attack
    @staticmethod
    def test_attack_initialization():
        attack = Attack(dmg=100, acc=75, crt=1.5, types=[AttackType.FIRE, AttackType.PHYSICAL])

        assert attack.dmg == 100
        assert attack.acc == 75
        assert attack.crt == 1.5
        assert attack.types == [AttackType.FIRE, AttackType.PHYSICAL]
        assert isinstance(attack.atk_str, LString)
        assert attack.atk_str == LString("Unspecified attack landed.")

    @staticmethod
    def test_attack_with_custom_lstring():
        custom_lstring = LString("Custom attack message.")
        attack = Attack(dmg=50, atk_str=custom_lstring)

        assert attack.atk_str == custom_lstring

