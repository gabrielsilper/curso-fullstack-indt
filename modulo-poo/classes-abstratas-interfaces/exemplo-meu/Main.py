from PessoaRepository import PessoaRepository
from Pessoa import Pessoa

pessoaRepository = PessoaRepository()

print(pessoaRepository.getNameTable())

print(pessoaRepository.countAll())

pessoa1 = Pessoa("Gabriel", 27)
pessoa2 = Pessoa("Fulano", 32)

pessoaRepository.save(pessoa1)
pessoaRepository.save(pessoa2)

print(pessoaRepository.countAll())

print(pessoaRepository.findAll())

print(pessoaRepository.findById(1))
