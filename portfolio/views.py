from django.shortcuts import render, redirect, get_object_or_404
from .models import FamilyMember, CryptoAsset
from .services import get_crypto_prices


def dashboard(request):
    member = FamilyMember.objects.all()
    crypto_ids_set = set()
    member_data = []
    for each_member in member:
        for each_asset in each_member.assets.all():
            crypto_ids_set.add(each_asset.crypto_id)

    crypto_ids_list = list(crypto_ids_set)

    
    prices = get_crypto_prices(crypto_ids_list)

    for each_member in member:
        patrimonio_membro = 0
        for each_asset in each_member.assets.all(): 
            valor_ativo = each_asset.quantity * prices[each_asset.crypto_id]['brl']
            patrimonio_membro += valor_ativo

        dados_do_membro = {
                'member': each_member,
                'patrimonio': patrimonio_membro
            }
        member_data.append(dados_do_membro)

    patrimonio_total = sum(item['patrimonio'] for item  in member_data)

    contexto = {
        'member_data': member_data,
        'patrimonio_total': patrimonio_total
    }
    return render(request, 'portfolio/dashboard.html', contexto)


def member_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        relationship = request.POST.get('relationship')
        member = FamilyMember(name=name, relationship=relationship)
        member.save()
        return redirect('dashboard')
    return render(request, 'portfolio/member_form.html', {})     


def member_edit(request, id):
    member = get_object_or_404(FamilyMember, id=id )
     
    if request.method == 'POST':
        member.name = request.POST.get('name')
        member.relationship = request.POST.get('relationship')
        member.save()
        return redirect('dashboard')
    
    return render(request, 'portfolio/member_form.html', {'member': member})


def member_delete(request, id):
    member = get_object_or_404(FamilyMember, id=id)
    
    if request.method == 'POST':
        member.delete()
        return redirect('dashboard')
    
    return render(request, 'portfolio/member_confirm_delete.html', {'member': member})


def asset_create(request, member_id):
    member = get_object_or_404(FamilyMember, id=member_id)

    if request.method == 'POST':
        crypto_id = request.POST.get('crypto')
        quantity = request.POST.get('quantity')

        crypto = CryptoAsset(crypto_id=crypto_id, quantity=quantity, member=member)
        crypto.save()
        return redirect('dashboard')
    return render(request, 'portfolio/asset_form.html', {'member': member})


def asset_edit(request, id):
    asset = get_object_or_404(CryptoAsset, id=id)

    if request.method == 'POST':
        asset.crypto_id = request.POST.get('crypto')
        asset.quantity = request.POST.get('quantity')
        asset.save()
        return redirect('dashboard')
    return render(request, 'portfolio/asset_form.html', {'asset': asset})

def asset_delete(request, id):
    asset = get_object_or_404(CryptoAsset, id=id)

    if request.method == 'POST':
        asset.delete()
        return redirect("dashboard")
    return render(request, 'portfolio/asset_confirm_delete.html', {'asset': asset})    