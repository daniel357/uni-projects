//
// Created by User on 5/18/2022.
//

#include "SortedMultiMap.h"
#include "SMMIterator.h"
#include <iostream>
#include <vector>
#include <exception>
using namespace std;

//O(n)
SortedMultiMap::SortedMultiMap(Relation r) {
    m = 500;
    length = 0;
    rel = r;
    pos = -1;
    first_empty = 0;
    next = new int[m];
    next_slla = new int[m];
    head_slla = -1;
    T = new Element[m];

    for (int i = 0; i < m - 1; i++) {
        next[i] = i + 1;
        next_slla[i] = i + 1;
        T[i].key = NULL_TVALUE;
        T[i].val = new TValue[m];
        T[i].size = 0;
    }
    // am initializat sfarsiturile de array cu -2 si nu cu -1 pt a nu se incurca cu elm din tabel care sunt singure in sirul inlantuit de valori cu acelasi hash
    next[m - 1] = -2;
    next_slla[m - 1] = -2;
    T[m - 1].key = NULL_TVALUE;
    T[m - 1].val = new TValue[m];
    T[m - 1].size = 0;
}

//O(n^4)
void SortedMultiMap::resize_rehash() {
    auto* cop_T = new Element[m]; //copy all the elements
    auto* cop_next = new int[m];
    auto* cop_next_slla = new int[m];
    for (int i = 0; i < m; i++) {
        cop_T[i] = T[i];
        cop_next[i] = next[i];
        cop_next_slla[i] = next_slla[i];
    }

    // deleting the old vectors
    delete[] T;
    delete[] next;
    delete[] next_slla;

    m *= 2; //double the quantity
    T = new Element[m];
    next = new int[m];
    next_slla = new int[m];

    // initializing
    for (int i = 0; i < m - 1; i++) {
        next[i] = i + 1;
        next_slla[i] = i + 1;
        T[i].key = NULL_TVALUE;
        T[i].val = new TValue[m];
        T[i].size = 0;
    }
    next[m - 1] = -2;
    next_slla[m - 1] = -2;
    T[m - 1].key = NULL_TVALUE;
    T[m - 1].val = new TValue[m];
    T[m - 1].size = 0;

    first_empty = 0;
    head_slla = -1;

    // moving the values in the new vectors, using the new hash function
    for (int i = 0; i < m / 2; i++) {
        // add the elements to the new vector add(key, value)
        for (int j = 0; j < cop_T[i].size; j++) {
            add(cop_T[i].key, cop_T[i].val[j]);
        }
    }
    // delete the copies
    delete[] cop_T;
    delete[] cop_next;
    delete[] cop_next_slla;
}

//O(n^3) - bc of the rehash from the while
void SortedMultiMap::add(TKey c, TValue v) {
    if (c < 0) {
        return;
    }
    pos = h(c); //get the position using the hash function

    // CASE 1: the table is empty
    if (isEmpty()) {
        if (pos == first_empty) {
            // if after the hash function pos equals the first empty, then first empty has to go to the next empty position
            first_empty = next[first_empty];
        }
        else {
            // have to change the links between the empty positions so that it would jump over the new added position
            int current_pos = first_empty;
            while (next[current_pos] != pos) {
                // current = last empty position before the position to add
                current_pos = next[current_pos];
            }
            next[current_pos] = next[pos]; //last empty position before the current one will point to the first empty position from the current one
            next_slla[current_pos] = next_slla[pos];
        }

        next[pos] = -1; //there is only one element with that value from hash
        T[pos].key = c; //adding the key to the table
        T[pos].val[T[pos].size] = v;
        T[pos].size++;
        head_slla = pos; //the element will be located at the head
        next_slla[head_slla] = -2; //we mark it as the last element from the linked list array
        length++;
        return;
    }

        // CASE 2: if positon where to add the element is empty, but the table is not empty
    else if (T[pos].key == NULL_TVALUE) {

        if (pos == first_empty) {
            first_empty = next[first_empty];
        }
        else {
            // have to change the links between the empty positions so that it would jump over the new added position
            int current_pos = first_empty;
            while (next[current_pos] != pos) {
                current_pos = next[current_pos];
            }
            next[current_pos] = next[pos];
            next_slla[current_pos] = next_slla[pos];
        }
        next[pos] = -1; //there is only one element with that value in the hash
        T[pos].key = c; //add the key to the table
        T[pos].val[T[pos].size] = v;// append the value corresponding to that key
        T[pos].size++;

        // actualizare pozitii slla
        // trebuie verificata relatia dintre chei pt next_slla
        int current = head_slla;
        // adaugare pe prima pozitie din slla
        if (!rel(T[head_slla].key, c)) {
            head_slla = pos; //head va deveni poz noului elm
            next_slla[pos] = current; //elm adaugat va pointa spre fostul head
            length++;
            return;
        }

        // verificare daca e un singur elm in lista => next_slla va fi -2 (invalid)
        if (next_slla[current] == -2) {
            next_slla[current] = pos;
            next_slla[pos] = -2;
            length++;
            return;
        }

        // altfel, se cauta pozitia pe care trebuie adaugat elm in slla
        while (rel(T[next_slla[current]].key, c)) {
            current = next_slla[current];
            if (next_slla[current] == -2) {
                // adaugare pe ultima poz din slla
                next_slla[current] = pos; //ultimul elm va pointa spre elm adaugat
                next_slla[pos] = -2; //elm adaugat e ultimul elm din lista
                length++;
                return;
            }
        }
        // adaugare pe alta poz in array
        next_slla[pos] = next_slla[current];
        next_slla[current] = pos;
        length++;
        return;

    }
        // CASE 3: poz nu e libera => vf dc sunt egale cheile
    else {
        int current_t = pos; //poz curenta din tabel
        int added_pos_t = first_empty;
        bool found = false;

        // CASE 3.1: elementul se afla pe pozitia care trebuie
        // => adica este primul din sirul inlantuit de valori cu acelasi hash
        if (h(T[current_t].key) == current_t) {
            while (current_t != -1) {
                if (T[current_t].key == c) {
                    // valoarea trebuie adaugata la vectorul de val al cheii
                    for (int i = 0; i < T[current_t].size; i++) {
                        // daca s-a gasit => nu se mai adauga
                        if (T[current_t].val[i] == v) {
                            return;
                        }
                    }
                    T[current_t].val[T[current_t].size] = v;
                    T[current_t].size++;
                    found = true;
                    length++;
                    return;
                }

                if (next[current_t] == -1) {
                    break; //pt a se pastra poz ultimului elm din sir
                }
                current_t = next[current_t];
            }
            if (!found) {
                // trebuie adaugata valoarea la sfarsitul sirului inlantuit de val cu acelasi hash
                if (first_empty == -2) {
                    // daca s-a umplut tabelul => resize and rehash
                    // retribuire valori, pt ca first_empty si pos si-au schimbat val
                    resize_rehash();
                    pos = h(c);
                    current_t = pos;
                    while (current_t != -1) {
                        current_t = next[current_t];
                    }

                    added_pos_t = first_empty;

                }
                T[added_pos_t].key = c; //adaugare in tabel
                T[added_pos_t].val[T[added_pos_t].size] = v;
                T[added_pos_t].size++;
                first_empty = next[first_empty]; //first_empty se muta pe urm poz libera
                next[current_t] = added_pos_t;
                next[added_pos_t] = -1; //elm va fi ultimul din sirul inlantuit
            }
        }

            // CAZ 2.2: elm de pe pos face parte dintr-un alt sir inlantuit cu hash diferit fata de pos
        else {
            if (first_empty == -2) {
                // daca s-a umplut tabelul => resize and rehash
                resize_rehash();
                pos = h(c);
                current_t = pos;
                added_pos_t = first_empty;
            }
            int i = 0; //i - va fi poz elm de dinaintea celui de pe pos
            // parcurgere array pana ajung la elm care pointeaza spre elm de pe pos
            while (next[i] != pos) {
                i++;
            }
            // mutare elm de pe pos pe noua pozitie, pt a se putea pune acolo elm cu hash = pos
            T[added_pos_t].key = T[pos].key;
            T[added_pos_t].val = T[pos].val;
            next[i] = added_pos_t;
            // actualizare poz in slla
            int current = head_slla; //parcurg vectorul next_slla pt a gasi poz ce pointa spre pos
            while (next_slla[current] != pos) {
                current = next_slla[current];
            }
            next_slla[current] = added_pos_t; //pozitia va pointa acum spre noua pozitie a elm
            first_empty = next[first_empty];
            next[added_pos_t] = next[pos];
            added_pos_t = pos;

            // adaugare elm nou pe pos
            T[pos].key = c;
            T[pos].val[T[pos].size] = v;
            T[pos].size++;

        }

        // actualizare valori pt slla
        // CAZ 1: cheia exista (nu se mai verifica dc si v este in vectorul val, pt ca e vf mai sus)
        int current = head_slla;

        // adaugare pe prima poz din slla
        if (!rel(T[head_slla].key, c)) {
            head_slla = added_pos_t; //head va deveni poz noului elm
            next_slla[added_pos_t] = current; //elm adaugat va pointa spre fostul head
            length++;
            return;

        }

        // cautare in functie de relatie, locul unde trebuie adaugat elm
        while (rel(T[next_slla[current]].key, c)) {
            current = next_slla[current];
            if (next_slla[current] == -2) {
                // adaugare pe ultima poz din slla
                next_slla[current] = added_pos_t; //ultimul elm va pointa spre elm adaugat
                next_slla[added_pos_t] = -2; //elm adaugat pe ultimul elm din lista
                length++;
                return;
            }
        }
        // adaugare pe alta poz in array
        // refacere conexiuni
        next_slla[added_pos_t] = next_slla[current];
        next_slla[current] = added_pos_t;
        length++;
        return;

    }
}


vector<TValue> SortedMultiMap::search(TKey c) {

    vector<TValue> values;
    if (c < 0) {
        return values;
    }

    pos = h(c);
    int current = pos;

    if (isEmpty()) {
        return values;
    }

    // cautare cheie prin toate elm cu acelasi hash
    while (current != -2) {
        if (T[current].key == c) {
            for (int i = 0; i < T[current].size; i++) {
                values.push_back(T[current].val[i]);
            }
            return values;
        }
        current = next[current];
    }
    // daca s-a ajuns aici => cheia nu s-a gasit
    return vector<TValue>();
}

//O(n^3) - din cauza parcurgerii vectorului de valori pt o anumita cheie
bool SortedMultiMap::remove(TKey c, TValue v) {
    //TODO - Implementation
    if (isEmpty() || c < 0) {
        return false;
    }

    pos = h(c);
    int current_t = pos;
    bool found_one = false; //daca s-a gasit valoarea si este unica in vectorul val al cheii c
    bool found_many = false; //daca s-a gasit val intr-un vector de val cu lungime > 1 al cheii c

    // CAZ 1: exista o singura cheie pe poz h(c)
    if (next[current_t] == -1) {
        if (T[pos].key == c) {
            // daca e un singur elm si se afla chiar pe poz h(c)
            // CAZ 1.1: cheia are o singura val in vectorul de valori
            if (T[pos].size == 1) {
                // daca e un singur elm si e egal cu v => se sterge si cheia
                if (T[pos].val[0] == v) {
                    T[pos].key = NULL_TVALUE;
                    T[pos].size = 0;
                    T[pos].val[0] = T[pos].val[1];

                    // legam poz de ultima din sirul de poz libere
                    if (first_empty == -2) {
                        // dc e plin tabelul => pos va ajunge first empty
                        first_empty = pos;
                    }
                    else {
                        // altfel, cautam ultima pozitie libera pentru a o putea lega de pos
                        int current_free = first_empty;
                        while (next[current_free] != -2) {
                            current_free = next[current_free];
                        }
                        next[current_free] = pos;
                        next_slla[current_free] = pos;
                    }
                    // actualizare poz in slla
                    if (pos == head_slla) {
                        // se sterge elm de pe head => urm va deveni head
                        head_slla = next_slla[head_slla];
                    }
                    else {
                        // altfel, cautam poz care pointeaza spre pos (=current)
                        int current = head_slla;
                        while (next_slla[current] != pos) {
                            current = next_slla[current];
                        }
                        next_slla[current] = next_slla[pos];
                    }

                    next[pos] = -2; //pt ca e pe ultima poz goala
                    next_slla[pos] = -2;
                    length--;
                    return true;
                }
                else {
                    return false;
                }
            }

                // CAZ 1.2: mai sunt elemente in vectorul de valori
                // caut v in vectorul de valori ai cheii; dc se gaseste => sterge doar val; altfel => return false
            else {
                for (int i = 0; i < T[pos].size; i++) {
                    if (T[pos].val[i] == v) {
                        for (int j = i; j < T[pos].size - 1; j++) {
                            T[pos].val[j] = T[pos].val[j + 1];
                        }
                        T[pos].size--;
                        length--;
                        return true;
                    }
                }
                return false;
            }
        }

        else {
            return false;
        }
    }

        // CAZ 2: sunt mai multe pozitii care au acelasi hash
    else {
        while (current_t != -1) {
            if (T[current_t].key == c) {

                // CAZ 2.1: cheia are o singura val in vectorul de valori
                if (T[current_t].size == 1) {
                    // daca e un singur elm si e egal cu v => se sterge si cheia
                    if (T[current_t].val[0] == v) {
                        int deleted_pos; //poz care se va pune la sf secventei de poz libere

                        if (current_t == pos) {
                            // se sterge elm de pe prima poz din acel sir inlantuit de chei
                            // => urmatorul elm va ajunge pe pozitia h(c) (trebuie mutat in locul elm sters)
                            // => pozitia acestuia va fi legata de ultima poz libera
                            T[current_t].key = T[next[current_t]].key;
                            T[current_t].size = T[next[current_t]].size;
                            T[current_t].val = T[next[current_t]].val;
                            deleted_pos = next[current_t];
                            next[current_t] = next[deleted_pos];
                            next_slla[current_t] = next_slla[deleted_pos];
                            T[deleted_pos].key = NULL_TVALUE;
                            T[deleted_pos].size = 0;
                            T[deleted_pos].val[0] = T[pos].val[1];
                        }

                        else {
                            // altfel, se cauta poz de dinaintea celei sterse si se fac conexiunile a.i. sa sara peste ea
                            // pozitia elm sters va fi legata de ultima poz libera
                            deleted_pos = pos;
                            while (next[deleted_pos] != current_t) {
                                deleted_pos = next[deleted_pos];
                            }
                            next[deleted_pos] = next[current_t];
                            next_slla[deleted_pos] = next_slla[current_t];
                            T[current_t].key = NULL_TVALUE;
                            T[current_t].size = 0;
                            T[current_t].val[0] = T[pos].val[1];
                            deleted_pos = current_t;
                        }

                        // legam poz de ultima din sirul de poz libere
                        if (first_empty == -2) {
                            // dc e plin tabelul => current va ajunge first empty
                            first_empty = deleted_pos;
                        }
                        else {
                            // altfel, cautam ultima pozitie libera pentru a o putea lega de deleted_pos
                            int current_free = first_empty;
                            while (next[current_free] != -2) {
                                current_free = next[current_free];
                            }
                            next[current_free] = deleted_pos;
                            next_slla[current_free] = deleted_pos;
                        }
                        // actualizare poz in slla
                        if (deleted_pos == head_slla) {
                            // se sterge elm de pe head => urm va deveni head
                            head_slla = next_slla[head_slla];
                        }
                        else {
                            // altfel, cautam poz care pointeaza spre pos (=current)
                            int current = head_slla;
                            while (next_slla[current] != deleted_pos) {
                                current = next_slla[current];
                            }
                            next_slla[current] = next_slla[deleted_pos];
                        }

                        next[deleted_pos] = -2; //pt ca e pe ultima poz goala
                        next_slla[deleted_pos] = -2;
                        length--;
                        return true;
                    }
                    else {
                        return false;
                    }
                }

                    // CAZ 2.2: mai sunt elemente in vectorul de valori => daca se gaseste, se sterge doar val
                else {
                    for (int i = 0; i < T[current_t].size; i++) {
                        if (T[current_t].val[i] == v) {
                            for (int j = i; j < T[current_t].size - 1; j++) {
                                T[current_t].val[j] = T[current_t].val[j + 1];
                            }
                            found_many = true;
                            T[current_t].size--;
                            length--;
                            return true;
                        }
                    }
                }

            }
            else {
                current_t = next[current_t];
            }
        }
    }

    return false;
}

//theta(1)
int SortedMultiMap::size() const {
    //TODO - Implementation
    if (!isEmpty()) {
        return length;
    }
    return 0;
}

//theta(1)
bool SortedMultiMap::isEmpty() const {
    //TODO - Implementation
    if (length == 0) {
        return true;
    }
    return false;
}

SMMIterator SortedMultiMap::iterator() const {
    return SMMIterator(*this);
}

//O(n)
SortedMultiMap::~SortedMultiMap() {
    //TODO - Implementation
    for (int i = 0; i < m; i++) {
        //stergere vector dinamic de valori ai fiecarei chei
        delete[] T[i].val;
    }
    delete[] T;
    delete[] next;
    delete[] next_slla;

}

vector<TValue> SortedMultiMap::valueBag() const
{
    vector<TValue> values;
    SMMIterator iterator1 = this->iterator();
    iterator1.first();
    while(iterator1.valid())
    {
        TValue v =iterator1.getCurrent().second;
        values.push_back(v);
        iterator1.next();
    }
    return values;
}