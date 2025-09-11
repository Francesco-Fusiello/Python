{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNWy4yC9ZwFJsqYSe0r5Gyb"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "##Print"
      ],
      "metadata": {
        "id": "x0nStHj5u0Fh"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kBMVJ65bl_iV",
        "outputId": "3dca99ad-4e79-4ce9-bc02-e76670b27627"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1728\n"
          ]
        }
      ],
      "source": [
        "print(6*24*12)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(65-(4+3*3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zFIREbRbmLEC",
        "outputId": "d4bb51ef-a765-4cbe-944e-317fd20ccfa8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "52\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print((5+3*2)/(7+4*(9-3)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nXovoni4msnV",
        "outputId": "8442f397-ab91-48a1-cc99-a157133c7842"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.3548387096774194\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Le variabili"
      ],
      "metadata": {
        "id": "6jx1UDGFu-V7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = 7\n",
        "print(a)\n",
        "a = 5\n",
        "print(a)\n",
        "a = a*2\n",
        "a = a*2\n",
        "numero = a\n",
        "numero = numero + 1\n",
        "a = 12\n",
        "print(a)\n",
        "print(numero)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oYQcLPqCnbQD",
        "outputId": "70184430-804d-4565-c1ef-e83393cc357f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n",
            "5\n",
            "12\n",
            "21\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "eta =41  # int - ricordati di cambiarla ogni anno\n",
        "giorni_in_un_anno = 365.24 #bisestile ogni 4\n",
        "ore_in_un_giorno = 24\n",
        "minuti_in_un_ora = 60\n",
        "secondi_in_un_minuto = 60\n",
        "\n",
        "eta_in_secondi = eta * giorni_in_un_anno * \\\n",
        "  ore_in_un_giorno * minuti_in_un_ora * secondi_in_un_minuto\n",
        "\n",
        "print(eta_in_secondi)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fwel9UdlrQPz",
        "outputId": "b52ff74c-1005-4f55-a21b-cb66f56a64e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1293826176.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = \"ciao!\"\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R87DmGvqqs--",
        "outputId": "d9fb2e7c-ecab-42b1-bfe5-67d811494dce"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ciao!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = \"4+5\"\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FhoA18yEteEA",
        "outputId": "4cd9d1be-23fb-42e9-8442-c6f220dd024e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4+5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 'questo corso é \"top\"'\n",
        "b = \"questo prof ha un'aria top\"\n",
        "c = \"questo corso è \\\"bellissimo\\\". Comunque il prof è top.\"\n",
        "print(a)\n",
        "print(b)\n",
        "print(c)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vWJDyxGstnQk",
        "outputId": "5673b13b-5a9a-4c58-a8a6-5edbcb88f303"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "questo corso é \"top\"\n",
            "questo prof ha un'aria top\n",
            "questo corso è \"bellissimo\". Comunque il prof è top.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Ciao\" + \" \" + \"Andrea\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8vbNQ2Ljt-jb",
        "outputId": "64b26f68-36be-4e5c-9da4-a27082239e5d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ciao Andrea\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nome = \"Andrea\"\n",
        "messaggio = \"Ciao \"\n",
        "messaggio_da_stampare = messaggio + \" \" + nome\n",
        "print(messaggio_da_stampare)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r07ranPkvPYr",
        "outputId": "fd1f7da3-fa42-4c64-eb42-eeaeb9bd8fc3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ciao  Andrea\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = \"Andrea\"\n",
        "print(17 * a)\n",
        "print(a, 17, 2*a)\n",
        "print(\"Buongiorno\" , a)\n",
        "print(a + str(17))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3DbcVDHFvvhk",
        "outputId": "de119021-647d-47ba-d458-efd803ff9613"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "AndreaAndreaAndreaAndreaAndreaAndreaAndreaAndreaAndreaAndreaAndreaAndreaAndreaAndreaAndreaAndreaAndrea\n",
            "Andrea 17 AndreaAndrea\n",
            "Buongiorno Andrea\n",
            "Andrea17\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Indexing"
      ],
      "metadata": {
        "id": "EjZObknUyJoZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "s = \"Andrea\"\n",
        "print(s[0] + s[-3])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0vdNumj1v760",
        "outputId": "e248210a-28ef-459f-e0da-7eb06bbd60a6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ar\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s = \"Tanto va la gatta al lardo che ci lascia lo zampino \"\n",
        "print(s[3:15])\n",
        "print(s[1:])\n",
        "print(s[:10])\n",
        "print(s[-4:-2])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hzGrfC-3xVZY",
        "outputId": "7880376c-c6a6-452e-cbc9-cc8128273318"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "to va la gat\n",
            "anto va la gatta al lardo che ci lascia lo zampino \n",
            "Tanto va l\n",
            "in\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s = \"0123456789\"\n",
        "print(s+s[0:-1+1])"
      ],
      "metadata": {
        "id": "R7x1roDPygwY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1bd10e1f-cdd1-4ee3-8809-9372facde0d8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0123456789\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(s[:3] + s[3:])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "feB4qS_HxfYh",
        "outputId": "0024d036-0fe5-4c97-b1ce-ab54889ddba4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0123456789\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Metodi delle stringhe"
      ],
      "metadata": {
        "id": "_hcDZXQUyT2T"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "s = \"Tanto va la gatta al lardo che ci lascia lo zampino \"\n",
        "\n",
        "print(s.find(\"gatta\"))\n",
        "print(s.find(\"t\"))\n",
        "print(s.find(\"x\")) # non trovata\n",
        "print(str(15))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-cGhbzVjyJfn",
        "outputId": "79726ba2-8c5f-4f78-e51d-234ece748f1f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "12\n",
            "3\n",
            "-1\n",
            "15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(s.find(s))\n",
        "print(s.find(\"s\"))\n",
        "print(\"s\".find(s))\n",
        "print(s.find(''))\n",
        "print(s.find(s+ \"bla bla bla \")+ 1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jtBfNH73yyCa",
        "outputId": "4c3cf1f6-83eb-457d-8430-90a94fc81d5c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "36\n",
            "-1\n",
            "0\n",
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s = \"Tanto va la gatta al lardo che ci lascia lo zampino \"\n",
        "\n",
        "print(s.find('a', 9)) # avendo due parametri inizia a cercare dopo il secondo parametro cioè 9 infatti il risultato è 10\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KSnDUq1F0KIE",
        "outputId": "029f8407-d497-4dc2-b8f3-81d5259e05fa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s = \"Tanto va la gatta al lardo che la gatta ci lascia lo zampino \"\n",
        "key = \"gatta\"\n",
        "pos1 = s.find(key)\n",
        "pos2 = s.find(key, pos1 + 1)\n",
        "pos3 = s.find(key, s.find(key, s.find(key)+1)+1)\n",
        "print(pos2)\n",
        "print(pos3) #-1 perchè non latrova perchè non esiste"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OCEiJTJR1ubt",
        "outputId": "70d6bf27-c769-4e51-d169-5b8c0fb3d193"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "34\n",
            "-1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "###Tipi"
      ],
      "metadata": {
        "id": "DdlbbuOP4ZOc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = 12\n",
        "print(type(a)) #int\n",
        "\n",
        "b = 12.7\n",
        "print(type(b)) #float\n",
        "\n",
        "c = \"Ciao\"\n",
        "print(type(c)) #str\n",
        "\n",
        "d = True\n",
        "print(type(d)) #boolean\n",
        "\n",
        "d = False\n",
        "print(type(d)) #boolean"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wazqlcux2_7E",
        "outputId": "e5a21ffe-9ecf-4129-bc0c-6f1ec130cd53"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n",
            "<class 'float'>\n",
            "<class 'str'>\n",
            "<class 'bool'>\n",
            "<class 'bool'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "1bLjBMBc4WZK"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "d8KCLGmj8-4j"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}